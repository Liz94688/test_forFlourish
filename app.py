import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'test_forFlourish'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-suguw.mongodb.net/test_forFlourish?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
def welcome_page():
    return render_template("welcome_page.html")


@app.route('/register_user')
def register_user():
    return render_template("register_user.html")


@app.route('/login_user')
def login_user():
    return render_template("login_user.html")


@app.route('/user_record')
def user_record():
    return render_template("user_record.html")


@app.route('/search_plants')
def search_plants():
    return render_template("search_plants.html", plants=mongo.db.plants.find())


@app.route('/edit_record')
def edit_record():
    return render_template("edit_record.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True) 