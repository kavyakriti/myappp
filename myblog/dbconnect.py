from __future__ import print_function
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from mysql.connector import Error
from newsapi import NewsApiClient
import mysql.connector
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

try:
    connection = mysql.connector.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE, charset = "utf8")
    cursor = connection.cursor()
    newsapi = NewsApiClient(api_key=config('API_KEY'))
    categories=['entertainment','sports','business']
    for c in categories:
      topheadlines = newsapi.get_top_headlines(category=c, language='en', country='in')
      articles = topheadlines['articles']
      for a in articles:
        source = a['source']['name']
        author = a['author']
        title = a['title']
        description = a['description']
        url = a['url']
        urltoimage = a['urlToImage']   
        timestamp = a['publishedAt']
        content = a['content']
        category=c
    News.objects.create(category=category,source=source,author=author,title=title,description=description,url=url,urlToImage=urltoimage,publishedAt=timestamp,content=content)
    connection.commit()

except mysql.connector.Error as error:
    print("Failed to insert into MySQL table {}".format(error))

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
  






