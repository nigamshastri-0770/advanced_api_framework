import psycopg2


class Database:

    def __init__(self, config):

        self.conn = psycopg2.connect(
            host=config["host"],
            port=config["port"],
            database=config["name"],
            user=config["user"],
            password=config["password"]
        )

        self.cursor = self.conn.cursor()

    def execute(self, query):

        self.cursor.execute(query)

        try:
            return self.cursor.fetchall()
        except:
            return []