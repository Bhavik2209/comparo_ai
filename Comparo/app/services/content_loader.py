from langchain_community.document_loaders import WebBaseLoader

def load_content(page_url):
    try:
        loader = WebBaseLoader(web_paths=[page_url], bs_get_text_kwargs={"separator": " ", "strip": True})
        load_content = loader.load()

        content = " ".join([doc.page_content for doc in load_content])

        return content
    except Exception as e:
        print(f"Error loading content from {page_url}: {e}")
        return ""