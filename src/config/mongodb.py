# General imports
import os
from dotenv import load_dotenv

# Utilitary imports
from flask_pymongo import PyMongo


mongo = PyMongo()


load_dotenv()

db_config = {
    'username': os.environ.get('MONGO_DB_USERNAME'),
    'password': os.environ.get('MONGO_DB_PWD'),
    'db': os.environ.get('MONGO_DB_NAME'),
}
