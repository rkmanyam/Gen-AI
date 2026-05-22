from mcp.server.fastmcp import FastMCP
from datastore import BOOKS

mcp = FastMCP(
        name="mcp-streamable-http",
        host="0.0.0.0",
        port=8000
    )

@mcp.tool(name = "search_books")
def search_books(query_string: str, genre: str = "") -> list[dict]:
    """ Searches books from the datastore based on the query string and genre
    
    Args:
        query_string(str): The search query string to match against book titles, authors, and tags.
        genre(str): Optional genre filter to narrow down search results.
    Returns:
        list[dict]: A list of books based on the query string and genre filter.
    """

    results = []
    q = query_string.lower()
    genre = genre.lower()
    for book in BOOKS.values():
        if not book["Is_Active"]:
            continue
        hit = ( 
                q in book["Title"].lower()
                or q in book["Author"].lower()
                #or any (q in [tag.lower() for tag in book["Tags"]])
            )
        genre_hit = (
                    genre and
                    any (genre in [g.lower() for g in book["Genres"]])
                )

        if hit or genre_hit:
            results.append(book)
    
    return results or [{"message": "No Book found"}]

def main():
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()
