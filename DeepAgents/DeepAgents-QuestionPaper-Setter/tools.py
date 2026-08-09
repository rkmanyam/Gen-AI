from tavily import TavilyClient
from dotenv import load_dotenv
import os
from langchain.tools import tool


load_dotenv()


@tool(parse_docstring=True)
def web_search(userquery: str):
    """
    Search the web for current or external information using Tavily.

    Use this tool when the user's request requires information that may be
    current, time-sensitive, externally verifiable, or not available in the
    agent's existing knowledge. Read the user query {userquery} carefully and search the web.

    Args:
        userquery: A concise and specific search query describing the information
            that needs to be found. Include important names, topics, dates,
            products, organizations, or other relevant context. Do not pass
            the entire user conversation; provide only the search query.

    Returns:
        Search results from Tavily containing relevant web information that can
        be used to answer the user's request. If no relevant results are found,
        return an appropriate indication that the search did not find useful
        information.

    Use web search for:
    - Current or recent information.
    - News, events, announcements, or updates.
    - Information about companies, products, people, or organizations.
    - Technical documentation or information that may have changed.
    - Facts that require verification from external sources.
    - Information not available in the agent's existing context.

    Do not use web search for:
    - Simple reasoning or calculations that do not require external data.
    - Information already provided by the user.
    - Tasks that can be completed using the agent's other available tools.

    Search guidelines:
    - Formulate a focused query rather than a vague or overly broad query.
    - Include relevant context such as dates, versions, or names when needed.
    - Prefer separate searches when the user's request contains multiple
      unrelated topics.
    - Do not fabricate information if the search results are insufficient.
    """

    client = TavilyClient(os.getenv('TAVILY_API_KEY'))
    response = client.search(
        query="Get 5 reasoning questions available in interner for 10th class students",
        search_depth="advanced"
    )

    return response