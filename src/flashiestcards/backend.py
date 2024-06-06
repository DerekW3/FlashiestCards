import sqlite3
from datetime import datetime


def establish_db_connection() -> sqlite3.Connection | None:
    try:
        connection = sqlite3.connect("flashcards.db")
        return connection
    except sqlite3.Error as e:
        print(f"Error establishing database connection: {e}")
        return None
