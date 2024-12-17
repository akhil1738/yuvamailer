from flask import Flask
import smtplib
from email.mime.text import MIMEText
import pyrebase
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
  
    config = {
      "apiKey": "AIzaSyB1w5Z-mhdwgK2Q_IAl5OfCmFdq9BHZH2I",
      "authDomain": "savesoil-87f59.firebaseapp.com",
      "databaseURL": "https://savesoil-87f59-default-rtdb.firebaseio.com",
      "projectId": "savesoil-87f59",
      "storageBucket": "savesoil-87f59.firebasestorage.app",
      "messagingSenderId": "599511712569",
      "appId": "1:599511712569:web:6c0b343b7d0b4309681ee8",
      "measurementId": "G-93CJXMS17G"
    }

    firebase = pyrebase.initialize_app(config)

    db = firebase.database()

    users = db.child("Email").get()
    email = users.val()

    time.sleep(4)

    subject = "Hello,"
    body = "Hello, This is a test Mail"

    sender = "iamyuva.org@gmail.com"
    recipients = [email]
    password = "svkk nskz tvxt wnib"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
  
    return email

if __name__ == '__main__':
    app.run()
