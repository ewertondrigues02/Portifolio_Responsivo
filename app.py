from pickle import TRUE
from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__name__':
    app.run(debug=TRUE)

