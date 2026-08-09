from langchain.chat_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()



def get_model() -> BaseChatModel:

    model = ChatGoogleGenerativeAI(
        model = os.getenv("GEMINI_MODEL_ID"),

    )

    return model