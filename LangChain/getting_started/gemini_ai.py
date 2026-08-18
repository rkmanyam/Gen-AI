from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()


agent = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash-lite"
)

response = agent.invoke("What is capital of France?")

print(response.text)