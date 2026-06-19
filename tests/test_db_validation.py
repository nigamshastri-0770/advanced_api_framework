# File: tests/test_db_validation.py

from core.database import (
Database
)

from validators.db_validator import (
DBValidator
)

def test_db_validation():
    db = Database()

    try:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER,
                name TEXT
            )
            """
        )

        db.execute(
            """
            DELETE FROM users
            """
        )

        db.execute(
            """
            INSERT INTO users
            VALUES(
                1,
                'Nigam'
            )
            """
        )

        row = db.fetch_one(
            """
            SELECT name
            FROM users
            WHERE id=1
            """
        )

        api_name = "Nigam"

        DBValidator.validate_equal(api_name, row[0])

    finally:
        db.close()
