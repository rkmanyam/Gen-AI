import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from typing import Any
import json

load_dotenv()

def get_connection() -> MySQLConnection:
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

def add_book(
    book_id: str,
    title: str,
    author: str,
    isbn: str,
    genre: str,
    available_copies: int
    ) -> str:
    
    with get_connection() as connection:
        with connection.cursor() as cursor:
            query: str = """
                INSERT INTO books(
                book_id,
                title,
                author,
                isbn,
                genre,
                available_copies
                )
                VALUES (%s,%s,%s,%s,%s,%s)
            """
            book_data = (
                book_id,
                title,
                author,
                isbn,
                json.dumps(genre),
                available_copies
            )
            cursor.execute(query, book_data)
            connection.commit()
            return f"Book {title} added successfully"

if __name__ == "__main__":
    add_book(
        "102",
        "AI Test",
        "Ram",
        "12349311",
        ["Edu"],
        5
    )