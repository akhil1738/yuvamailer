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

    subject = "Hello,"
    body = "Hello, This is a test Mail" 
    
    sender = "iamyuva.org@gmail.com"
    recipients = ["yuvalabs@gmail.com"]
    password = "svkk nskz tvxt wnib"
       
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
  
    return emailid

if __name__ == '__main__':
    app.run()
