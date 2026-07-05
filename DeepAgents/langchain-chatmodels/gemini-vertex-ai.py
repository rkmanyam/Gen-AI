from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model = os.getenv('GOOGLE_GENAI_MODEL'),
    project = os.getenv('GOOGLE_PROJECT_ID')
)

response = llm.invoke("What is capital of France?")

print(response.content)