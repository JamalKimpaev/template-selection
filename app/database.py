from tinydb import TinyDB
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PATH = os.path.join(BASE_DIR, 'db.json')

db = TinyDB(PATH)
