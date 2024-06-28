# test_db_connection.py

from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv

load_dotenv()

TECH_HUB_MYSQL_USER = getenv('TECH_HUB_MYSQL_USER')
TECH_HUB_MYSQL_PWD = getenv('TECH_HUB_MYSQL_PWD')
TECH_HUB_MYSQL_HOST = getenv('TECH_HUB_MYSQL_HOST')
TECH_HUB_MYSQL_DB = getenv('TECH_HUB_MYSQL_DB')

# engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
engine = create_engine('mariadb+mariadbconnector://{}:{}@{}/{}'.
                       format(TECH_HUB_MYSQL_USER,
                              TECH_HUB_MYSQL_PWD,
                              TECH_HUB_MYSQL_HOST,
                              TECH_HUB_MYSQL_DB))

connection = engine.connect()
print("Connection successful")
connection.close()