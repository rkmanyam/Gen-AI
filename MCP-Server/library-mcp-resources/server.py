from mcp.server.fastmcp import FastMCP
from datastore import BOOKS
from datastore import STUDENTS

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


@mcp.resource("college://students/{student_roll_number}")
def get_student_info(student_roll_number: str) -> dict:
    """ Retrieves Student Information based on Stundent roll number
    
    Args(string):
    student_roll_number(str): The roll number of the student to retrieve information for.

    Returns:
    dict: A dictionary containing the student's information, or a message if the student is not found.

    """
    student_info = STUDENTS.get(student_roll_number)
    if student_info:
        return student_info
    else:
        return {"message": "Student not found"}


@mcp.prompt()
def suggest_books_based_on_genre(genre: str) -> dict:
    return f"""
    You are a librarian assistant. 
    Based on the genre provided {genre}, suggest 3 books from the datastore that match the genre.

    Include:
    - Title
    - Author
    - Genres
    - Why it matches the user preference
    """

def main():
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()
