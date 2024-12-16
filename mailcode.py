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
    get_url = driver.current_url 
    url = get_url
    driver.quit()
    parsed_url = urlparse(url)
    emailid = parsed_url[4]    

    time.sleep(5)
  
    return emailid

if __name__ == '__main__':
    app.run()
