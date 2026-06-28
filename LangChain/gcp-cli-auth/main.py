from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    model = ChatGoogleGenerativeAI(
        model = "gemini-3.5-flash",
        project = os.getenv("PROJECT_ID")
    )
    result = model.invoke("What is capital of France")
    result.pretty_print()

if __name__ == "__main__":
    main()