from pickle import TRUE
from flask import Flask, render_template, redirect
from flask import mail, message
from config import email,senha



app = Flask(__name__)
app.secret_key = 'portifolio'

mail_settings = {
    "MAIL_SERVER": 'smtp.gamil.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
}


@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__name__':
    app.run(debug=TRUE)

