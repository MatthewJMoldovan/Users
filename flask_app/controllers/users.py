from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import Peoples


@app.route('/')
def index():
    return render_template("index.html", all_users = Peoples.get_all())


@app.route('/add_user')
def add_user():
    return render_template("add_user.html")


@app.route('/create_user', methods=['POST'])
def create_user():
    Peoples.create_user(request.form)
    return redirect('/')