import sqlite3
from typing import Any


def establish_db_connection() -> sqlite3.Connection:
    try:
        db_connection: sqlite3.Connection = sqlite3.connect("flashcards.db")
        return db_connection
    except sqlite3.Error as e:
        print(f"Error establishing database connection: {e}")
        raise e


def create_flashcards_table():
    try:
        db_connection: sqlite3.Connection = establish_db_connection()
        db_cursor: sqlite3.Cursor = db_connection.cursor()

        db_cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS flashcards(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question VARCHAR(255) NOT NULL,
            answer VARCHAR(255) NOT NULL
        )
        """
        )
        db_connection.commit()
        db_cursor.close()

    except sqlite3.Error as e:
        print(f"Error creating flashcards table: {e}")


def execute_sql_query(query, parameters=None) -> list[Any]:
    try:
        db_connection: sqlite3.Connection = establish_db_connection()
        db_cursor: sqlite3.Cursor = db_connection.cursor()

        if parameters:
            db_cursor.execute(query, parameters)
        else:
            db_cursor.execute(query)

        db_connection.commit()
        results: list[Any] = db_cursor.fetchall()
        db_cursor.close()

        return results

    except sqlite3.Error as e:
        print(f"Error executing SQL query: {e}")
        return []
