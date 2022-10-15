# scr code in flask web site market digital inovation profesionality

from flask import Flask , request , render_template
from flask import url_for , redirect
import time
from flask_pymongo import PyMongo




app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://kwork:Password01@cluster0.dy9g7dk.mongodb.net/workdb?retryWrites=true&w=majority'


mongoup = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/home', methods=['GET', 'POST'])
def inhome():
    return render_template('index.html')



@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


if __name__ == "__main__":
    
    app.run(debug=True, port=5050)
