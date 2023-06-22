import os

import psycopg2
from psycopg2 import sql
from itemadapter import ItemAdapter


class PostgresqlPipeline:
    HOST = os.getenv("DB_HOST")
    DATABASE = os.getenv('DB_NAME')
    USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASS')

    DROP_FLATS_TABLE_IF_EXISTS_QUERY = sql.SQL("""
        DROP TABLE IF EXISTS flats
    """)
    CREATE_FLATS_TABLE_QUERY = sql.SQL("""
        CREATE TABLE IF NOT EXISTS flats (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            image_data INTEGER
        )
    """)
    INSERT_FLAT_QUERY = sql.SQL("""
        INSERT INTO flats (title, image_data) VALUES (%s, %s)
    """)

    def __init__(self):
        self.connection = None
        self.cursor = None
        self.flats_loaded = 0

    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host=self.HOST,
            database=self.DATABASE,
            user=self.USER,
            password=self.PASSWORD
        )
        self.cursor = self.connection.cursor()
        self.create_tables()

    def close_spider(self, spider):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def create_tables(self):
        self.cursor.execute(self.DROP_FLATS_TABLE_IF_EXISTS_QUERY)
        self.cursor.execute(self.CREATE_FLATS_TABLE_QUERY)
        self.connection.commit()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.cursor.execute(self.INSERT_FLAT_QUERY, (adapter.get('text'), 123))
        return item
