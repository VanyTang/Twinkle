from app import app
from app import mongo
from flask import render_template, request, flash, redirect, url_for, session


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


def login_check(name, pwd):
    if mongo.db['userinfo'].find({'name': name.lower(), 'pwd': pwd}).count() != 0:
        return True
    else:
        return False


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if login_check(request.form['inputName'], request.form['inputPassword']):
            session['username'] = request.form['inputName']
            return redirect(url_for('index'))
        else:
            flash("Invalid Username or Password")
            return render_template("login.html")
    elif request.method == "GET":
        return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
