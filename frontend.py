import chainlit as cl
import httpx

API_URL = "http://127.0.0.1:8000/api/v1/comparison/"

# Helper to render a product card
def render_product_card(product, is_best=False):
    title = product.get("title") or product.get("product_name")
    url = product.get("url")
    highlights = product.get("highlights") or product.get("specs_comparison")
    pros = product.get("pros", [])
    cons = product.get("cons", [])
    content = product.get("content") or product.get("reviews_summary")
    score = product.get("score", None)
    
    card_md = f"""
### {'🏆 ' if is_best else ''}{title}
{'[Product Link](' + url + ')' if url else ''}

**Highlights:**
"""
    if highlights:
        for k, v in highlights.items():
            card_md += f"- **{k}**: {v}\n"
    if pros:
        card_md += "\n**Pros:**\n"
        for p in pros:
            card_md += f"- ✅ {p}\n"
    if cons:
        card_md += "\n**Cons:**\n"
        for c in cons:
            card_md += f"- ❌ {c}\n"
    if content:
        card_md += f"\n**Summary:** {content}\n"
    if score is not None:
        card_md += f"\n**Score:** {score}\n"
    return card_md

@cl.on_message
async def main(message: cl.Message):
    user_query = message.content.strip()
    if not user_query:
        await cl.Message(content="Please enter a query to compare smartphones.").send()
        return
    # Show a loading message
    loading_msg = cl.Message(content="🔎 Comparing smartphones, please wait...")
    await loading_msg.send()
    # Prepare request
    payload = {"query": user_query, "max_results": 1}
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(API_URL, json=payload)
        if response.status_code != 200:
            await cl.Message(content=f"❌ Error: {response.text}").send()
            return
        data = response.json()
    except Exception as e:
        await cl.Message(content=f"❌ Failed to connect to backend: {e}").send()
        return
    # Remove loading message
    await loading_msg.remove()
    # Handle response
    if not data.get("success"):
        await cl.Message(content=f"❌ {data.get('message', 'Unknown error')}").send()
        return
    products = data.get("products", [])
    if isinstance(products, dict):
        products = products.get("products", [])
    best_product = data.get("best_product", {})
    comparison = data.get("comparison", [])
    youtube_link = data.get("youtube_link")
    # Show best product card first
    best_name = best_product.get("product_name")
    best_justification = best_product.get("justification")
    if best_name:
        # Find the best product in the list
        best = None
        for p in products:
            if (p.get("title") or p.get("product_name")) == best_name:
                best = p
                break
        if best:
            await cl.Message(content=render_product_card(best, is_best=True)).send()
        if best_justification:
            await cl.Message(content=f"**Why best?** {best_justification}").send()
    # Show other products as cards
    for p in products:
        pname = p.get("title") or p.get("product_name")
        if pname == best_name:
            continue
        await cl.Message(content=render_product_card(p)).send()
    # Show comparison table if available
    if comparison:
        table_md = "| Product | Processor | Battery | Camera | Display | Storage |\n|---|---|---|---|---|---|\n"
        for c in comparison:
            specs = c.get("specs_comparison", {})
            table_md += f"| {c.get('product_name','')} | {specs.get('processor','')} | {specs.get('battery','')} | {specs.get('camera','')} | {specs.get('display','')} | {specs.get('storage','')} |\n"
        await cl.Message(content="**Specs Comparison Table:**\n" + table_md).send()
    # Show YouTube link if available
    if youtube_link:
        await cl.Message(content=f"▶️ [Watch on YouTube]({youtube_link})").send()
    else:
        await cl.Message(content="No YouTube video found for the best product.").send()