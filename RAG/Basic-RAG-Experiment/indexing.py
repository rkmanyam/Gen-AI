from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from utils import get_embedding_model
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

def get_chunks(
        dir_path="./knowledge_base/text_base/", 
        glob_filter="**/*.txt", 
        loader_cls = TextLoader
        ) -> list[Document]:
    
    """
    This method load the documents from the knowledge base directories 
    and chunk them into pieces
    """

    documents = DirectoryLoader(
        path=dir_path,
        glob=glob_filter,
        loader_cls = loader_cls
    )

    splitter = RecursiveCharacterTextSplitter(
            chunk_size = 300,
            chunk_overlap=50
    )

    docs = documents.load_and_split(splitter)

    for doc in docs:
        doc.metadata['filename'] = docs[0].metadata['source'].split("\\")[-1].split(".")[0]

    return docs



def get_chroma_db(
        collection_name: str, 
        embedding_function: GoogleGenerativeAIEmbeddings,
        persist_directory_path: str = "./vector_databases/chroma-db") -> Chroma:

    """
    This method returns chroma_db
    """

    chroma_db = Chroma(
        collection_name = collection_name,
        embedding_function = embedding_function,
        persist_directory = persist_directory_path
    )

    return chroma_db



def indexing(
        dir_path:str,
        glob_filter:str,
        embedding_function:GoogleGenerativeAIEmbeddings,
        collection_name:str="sample-collection",
        persist_directory_path:str="./chroma-db",
        loader_cls = TextLoader) -> list[str]:

    """
    This method embedd the chunks into Vector Database
    """

    chunks = get_chunks(
        dir_path=dir_path,
        glob_filter=glob_filter,
        loader_cls= loader_cls,
    )

    

    chroma_db = get_chroma_db(
        collection_name=collection_name, 
        persist_directory_path=persist_directory_path,
        embedding_function=embedding_function)

    indexing = chroma_db.add_documents(documents=chunks)

    return indexing


if __name__ == "__main__":

    embedding_model=os.getenv("GOOGLE_EMBEDDING_MODEL")
    project=os.getenv("GOOGLE_PROJECT_ID")
    location=os.getenv("EMBEDDING_MODEL_LOCATION")
    chunks_indexing = indexing(
                dir_path="./knowledge_base/text_base/",
                glob_filter="**/*.txt",
                embedding_function=get_embedding_model(embedding_model=embedding_model, project=project, location=location),
                collection_name="sample-collection",
                persist_directory_path="./vector_databases/chroma-db",
                loader_cls = TextLoader,
    )

    print(chunks_indexing)