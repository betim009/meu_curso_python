import os

import mysql.connector
from dotenv import load_dotenv


load_dotenv()


def connection():
    return mysql.connector.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database"),
        port=int(os.getenv("port", "3306")),
        ssl_ca=os.getenv("ssl_ca"),
    )
