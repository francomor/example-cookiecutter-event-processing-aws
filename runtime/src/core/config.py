import os


# same default parameters as docker-composer mysql service
MYSQL_SERVER = os.getenv("MYSQL_SERVER", 'localhost')
MYSQL_USER = os.getenv("MYSQL_USER", 'user')
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", 'password')
MYSQL_DB = os.getenv("MYSQL_DB", 'database_name')
SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}/{MYSQL_DB}"
)
