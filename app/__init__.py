from flask import Flask
from config import Config
import psycopg2

app = Flask(__name__)
app.config.from_object(Config)
con  = psycopg2.connect(
    host="localhost",
    port="5432",
    database="kursah",
    user="postgres",
    password="volvo189724"
    )


from app import routes