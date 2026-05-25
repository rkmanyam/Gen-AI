import mysql.connector
import os
from dotenv import load_dotenv
from typing import Any
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

load_dotenv()



def get_connection() -> MySQLConnection:
    """Create and returns MySQL DB connection using variables"""
    return mysql.connector.connect(
        host = os.getenv("MYSQL_HOST", "localhost"),
        database = os.getenv("MYSQL_DATABASE", "library"),
        user = os.getenv("MYSQL_USER", "xxxxxxx"),
        password = os.getenv("MYSQL_PASSWORD", "xxxxxxxxx")
    )


def execute_query(query:str, params: tuple[Any, ...] = ()) -> list[tuple[Any, ...]]:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, params)

            if cursor.description:
                return cursor.fetchall()
            connection.commit()

        


if __name__ == "__main__":
    result = execute_query('select * from authors')
    print(result)
    

