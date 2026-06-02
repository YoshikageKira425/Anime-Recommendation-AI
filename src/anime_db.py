import chromadb

chroma_client = chromadb.PersistentClient("./data")
collection = chroma_client.get_or_create_collection("anime")
