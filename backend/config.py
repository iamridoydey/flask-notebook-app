import os

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
    MYSQL_USER = os.getenv("MYSQL_USER", "flaskuser")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD","flaskpass")
    MYSQL_DB = os.getenv("MYSQL_DB","notebookdb")
