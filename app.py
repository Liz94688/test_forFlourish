# Importing Modules
import os
from flask import Flask, render_template, flash, redirect, request, url_for, session, logging
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from wtforms import Form, BooleanField, StringField, TextAreaField, PasswordField, validators

# Declaring App Name
app = Flask(__name__)

# Configure MongoDB
app.config["MONGO_DBNAME"] = 'test_forFlourish'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-suguw.mongodb.net/test_forFlourish?retryWrites=true&w=majority'

mongo = PyMongo(app)

# Welcome Page
@app.route('/')
@app.route('/welcome_page')
def welcome_page():
    return render_template("welcome_page.html")


# Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

# Register
@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    form = RegisterForm(request.form)
    users = mongo.db.users
    if request.method == 'POST' and form.validate():
        # Check if the username already exists in the MongoDB collection

        # Insert input fields into MongoDB collection
        users.insert({
            'name': request.form['name'].lower(),
            'email': request.form['email'].lower(),
            'username': request.form['username'].lower(),
            'password': request.form['password'].lower
        })

        # Message to acknowledge registration and redirect to url_for Login
        
        return redirect(url_for('login_user'))
    return render_template('register_user.html', form=form)

# Login
@app.route('/login_user', methods=['GET' 'POST'])
def login_user():
    return render_template("login_user.html")

# User Account
@app.route('/user_account')
def user_account():
    return render_template("user_account.html")

# Search Plants
@app.route('/search_plants')
def search_plants():
    return render_template("search_plants.html", plants=mongo.db.plants.find())

# Plant Record
@app.route('/plant_record')
def plant_record():
    return render_template("plant_record.html")

# Edit User Plant Record
@app.route('/edit_user_plant_record')
def edit_user_plant_record():
    return render_template("edit_user_plant_record.html")

# Delete User Plant Record
# Log Out


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True) 