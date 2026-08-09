from langchain.chat_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_aws import ChatBedrockConverse
from dotenv import load_dotenv
import os

load_dotenv()



def get_model() -> BaseChatModel:

    # if os.getenv("PROVIDER").__contains__ == "AWS":

    #     print("Selecting AWS LLM Model")

    #     model = ChatBedrockConverse(
    #         model=os.getenv('AWS_BEDROCK_MODEL_ID'),
    #         api_key = os.getenv('AWS_BEARER_TOKEN_BEDROCK'),
    #         region_name="us-west-1"
    #     )

    #     return model

    # if os.getenv("PROVIDER").__contains__ == "GOOGLE":

    #     print("Selecting GOOOGLE LLM Model")

    model = ChatGoogleGenerativeAI(
        model = os.getenv("GEMINI_MODEL_ID"),
        #project = os.getenv('GOOGLE_PROJECT_ID'),
        #api_key= os.getenv('GEMINI_API_KEY'),
        
        
    )

    return model
