# File: core/database.py

import sqlite3

class Database:
    def __init__(
        self,
        db_path="test.db"
    ):
        self.connection = (
            sqlite3.connect(
                db_path
            )
        )

        self.cursor = (
            self.connection.cursor()
        )

    def execute(
        self,
        query,
        params=None
    ):
        self.cursor.execute(
            query,
            params or ()
        )

        self.connection.commit()

    def fetch_one(
        self,
        query,
        params=None
    ):
        self.cursor.execute(
            query,
            params or ()
        )

        return (
            self.cursor.fetchone()
        )

    def fetch_all(
        self,
        query,
        params=None
    ):
        self.cursor.execute(
            query,
            params or ()
        )

        return (
            self.cursor.fetchall()
        )

    def close(
        self
    ):
        self.connection.close()
