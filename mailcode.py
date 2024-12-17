from flask import Flask
import smtplib
from email.mime.text import MIMEText
from urllib.parse import urlparse
from selenium import webdriver 
import time
  


app = Flask(__name__)

@app.route('/')
def hello_world():
    driver = webdriver.Chrome() 
    url = "https://yuvalabs.in/"    
    driver.get(url)   
    get_url = driver.current_url 
    url1 = get_url
    driver.quit()

    return url1

if __name__ == '__main__':
    app.run()
