from flask import Flask
import smtplib
from email.mime.text import MIMEText
from urllib.parse import urlparse
from selenium import webdriver 
import time
  


app = Flask(__name__)

@app.route('/')
def hello_world():
    

    return "Hello World"

if __name__ == '__main__':
    app.run()
