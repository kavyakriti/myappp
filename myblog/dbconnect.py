from __future__ import print_function
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from newsapi import NewsApiClient
import json
import urllib3
import requests
import re
import MySQLdb
import os
from decouple import config       

HOST = config('DB_HOST')
USER = config('DB_USER')
PASSWORD = config('DB_PASSWORD')
DATABASE = config('DB_NAME') 
PORT = config('DB_PORT')

def store_data(articles, source, auther, title, description, url, timestamp, content):
    db = MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE, charset = "utf8")
    cursor = db.cursor()
    insert_query = MySQLdb.escape_string("INSERT INTO table (articles, source, author, title, description, url, timestamp, content) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(insert_query, (articles, source, auther, title, description, url, timestamp, content))
    db.commit()
    cursor.close()
    db.close()
    return

def on_data(data):
    try:
        datajson = json.loads(data)
        articles = datajson['articles']
        source = datajson['articles']['source']['name']
        author = datajson['articles']['auther']
        title = datajson['articles']['title']
        description = datajson['articles']['description']
        url = datajson['articles']['url']
        timestamp = parser.parse(datajson['articles']['publishedAt'])
        content = datajson['articles']['content']

        store_data(articles, source, author, title, description, url, timestamp, content)
    except Exception as e:           
        print(e)

if __name__ == '__main__':
    data = requests.get('https://newsapi.org/v2/top-headlines?country=us&config(API_KEY)')
    print("hiiii")
    on_data(data)
