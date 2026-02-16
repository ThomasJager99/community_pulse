from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

__all__ = [
    "db"
]

#NOTE: we create connection db. And when we want to take all from this file
# we will got only "db".
# from core.db import *




