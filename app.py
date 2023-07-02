from flask import Flask
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(".env")

app = Flask(__name__)


@app.route("/")
def hello():
    # # MySQLへの接続とクエリの実行
    connection = mysql.connector.connect(
        host=os.environ.get("HOST"),
        user=os.environ.get("USER"),
        password=os.environ.get("PASSWORD"),
        database=os.environ.get("DATABASE"),
        port=os.environ.get("PORT"),
    )
    connection
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sample_tb")
    results = cursor.fetchall()
    connection.close()

    return results


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
