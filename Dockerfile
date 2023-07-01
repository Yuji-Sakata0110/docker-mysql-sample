FROM python:3.9
FROM --platform=arm64 mysql:latest

ENV MYSQL_ROOT_PASSWORD=root

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y mysql-client

# 必要なPythonパッケージのインストール
RUN pip install Flask mysql-connector-python

# アプリケーションファイルの追加
COPY app.py /app/app.py

# Flaskアプリケーションの起動コマンド
CMD ["python", "-m", "/app/flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]