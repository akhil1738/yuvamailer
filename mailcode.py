from flask import Flask
import smtplib
from email.mime.text import MIMEText
#from urllib.parse import urlparse
#from selenium import webdriver 
import requests
import json
  


app = Flask(__name__)

@app.route('/')
def hello_world():
  
    url = "https://yuvalabs.in/"

    response = json.loads(requests.request("GET", url).text)

    url = response

    return url

if __name__ == '__main__':
    app.run()
