import os

import psycopg2
from psycopg2 import sql
from flask import Flask


app = Flask(__name__)


def get_flats() -> list:
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    cursor = connection.cursor()
    cursor.execute(sql.SQL("SELECT * FROM flats"))
    flats_db = cursor.fetchall()
    flats = [{
        "id": flat[0],
        "title": flat[1],
        "image": flat[2]
    } for flat in flats_db]
    connection.commit()
    cursor.close()
    connection.close()
    return flats


@app.route("/")
def landing_page():
    return get_flats()


if __name__ == '__main__':
    hostName = "0.0.0.0"
    serverPort = 8080
    print(f"\tStarting Flask server on {hostName}:{serverPort}\n")
    app.run(host=hostName, port=serverPort)
