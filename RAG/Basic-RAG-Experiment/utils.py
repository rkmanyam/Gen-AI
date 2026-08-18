from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()


def get_llm(model:str, project:str, location:str) -> ChatGoogleGenerativeAI:
    """
    This method provide the llm object
    """

    llm = ChatGoogleGenerativeAI(
        model = model,
        project = project,
        location=location
    )

    return llm

def get_embedding_model(embedding_model:str, project:str, location: str) -> GoogleGenerativeAIEmbeddings:
    """
    This method provide the embedding model
    """

    embedding_model = GoogleGenerativeAIEmbeddings(
        model = embedding_model,
        project= project,
        location=location
    )

    return embedding_model