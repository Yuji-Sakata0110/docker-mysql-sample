from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route("/")
def hello():
    # # MySQLへの接続とクエリの実行
    connection = mysql.connector.connect(
        host="docker-mysql-db-1",
        user="root",
        password="root",
        database="sample",
        port=3306,
    )
    connection
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sample_tb")
    results = cursor.fetchall()
    connection.close()

    return results


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
