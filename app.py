from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route("/")
def hello():
    # MySQLへの接続とクエリの実行
    connection = mysql.connector.connect(
        host="mysql",  # Dockerコンテナ名を指定
        user="root",
        password="root",
        database="sample",
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sample_tb")
    results = cursor.fetchall()
    connection.close()

    # 結果の表示
    output = ""
    for row in results:
        output += f"{row[0]}: {row[1]}\n"
    return output


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
