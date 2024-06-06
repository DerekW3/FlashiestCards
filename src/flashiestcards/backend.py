import sqlite3
from datetime import datetime
from sqlite3.dbapi2 import Cursor


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
        db_cursor: Cursor = db_connection.cursor()

    except sqlite3.Error as e:
        print(f"Error creating flashcards table: {e}")
