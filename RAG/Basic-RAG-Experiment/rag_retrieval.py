from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from indexing import get_chroma_db
from utils import get_llm, get_embedding_model
from dotenv import load_dotenv
import os

load_dotenv()


def rag_search(question:str, model:str, model_location:str, embedding_model:str, project:str, embedding_model_location:str):

    prompt = ChatPromptTemplate.from_template(
        """
        Answer the questions only ased on the context provided.
        Don't provide the answers out of the context. If the ask
        is out of the context, simply say, I'm bound to answer to
        questions only related to Remote work Policy and Shipping 
        related issues.

        context: {context}
        question: {question}

        Answer:
        """
    )


    llm = get_llm(
        model=model,
        project=project, 
        location=model_location)
    
    embedding_function=get_embedding_model(embedding_model=embedding_model, 
                                           project=project, 
                                           location=embedding_model_location)

    chroma_db = get_chroma_db(
        collection_name="sample-collection",
        embedding_function=embedding_function
    )

    context = chroma_db.as_retriever().invoke(question)


    chain = prompt | llm | StrOutputParser()

    answer = chain.invoke({
        "context": context,
        "question": question
    })

    return answer



if __name__ == "__main__":
    
    model=os.getenv("GEMINI_LLM_MODEL_ID")
    model_location=os.getenv("GOOGLE_LLM_MODEL_LOCATION")

    embedding_model=os.getenv("GOOGLE_EMBEDDING_MODEL")
    embedding_model_location=os.getenv("EMBEDDING_MODEL_LOCATION")

    project=os.getenv("GOOGLE_PROJECT_ID")

    question = input("Ask me about Remote Work Policy or Shipping related queries: ")

    answer = rag_search(
        question=question, 
        model=model,
        model_location=model_location,
        embedding_model=embedding_model,
        embedding_model_location=embedding_model_location,
        project=project)
    
    print(answer)

