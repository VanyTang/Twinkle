from app import app
from app import mongo
from flask import render_template, request, flash, redirect, url_for, session
from werkzeug.utils import secure_filename


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


def generate_filename(info):
    return info['title'] + ".pdf"


def save_file(f, info):
    # mongo.db.files.save()
    f.save(app.config['UPLOAD_FOLDER'] + generate_filename(info))
    return True


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        title = request.form['inputTitle']
        # author = request.form['inputAuthor']
        # publisher = request.form['inputPublisher']
        f = request.files['file']

        info = {'title': title,
                'uploader': session['username'],
                # 'author' : author,
                # 'publisher' : publisher
                }
        if save_file(f, info):
            return redirect(url_for('index'))
        else:
            flash("Upload Failed")
            return render_template('upload.html')
    else:
        return render_template('upload.html')


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
