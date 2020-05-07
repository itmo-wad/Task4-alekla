from app import app
from flask import Flask, request, redirect, url_for, render_template, jsonify, make_response
from resources.forms import  SignUpForm, SignInForm
import string, random
from models.models import User

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

allowed_file_extentions = ['jpeg', 'jpg', 'png']

@app.route('/')
def index():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        return redirect(url_for('cabinet'))
    else:
        return redirect(url_for('login'))

@app.route('/upload', methods = ['POST'])
def upload_file():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        f = request.files['file']
        if f.filename.split(".")[-1] in allowed_file_extentions:
            filename = id_generator(20) + f.filename.split(".")[-1]
            with open(filename) as output:
                output.write(f.bytes)
            return redirect(url_for('cabinet'))
    else:
        return jsonify(result={"status": 500})

@app.route('/cabinet', methods=['GET'])
def cabinet():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        user = User.objects.get(id=1)
        return render_template('cabinet.html',user=user)
    return redirect(url_for('signin'))

@app.route('/signup', methods=['GET'])
def signup():
    return redirect(url_for('signin'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    return redirect(url_for('login'))

@app.route('/logout')
def logout(response):
    del response.headers['Authorization']
    return response