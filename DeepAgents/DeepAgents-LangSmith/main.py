from deepagents import create_deep_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)

agent = create_deep_agent(
    #model="google_genai:gemini-3.5-flash",
    model=model,
    tools=[],
    system_prompt="You are a helpful assistant."
)
