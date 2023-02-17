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
    user_id = Peoples.create_user(request.form)
    return redirect(f'/show_user/{user_id}')

@app.route('/show_user/<int:id>')
def show_user(id):
    user = Peoples.get_one(id)
    return render_template("show_user.html", user = user)

@app.route('/update_user/<int:id>')
def update_user(id):
    user = Peoples.get_one(id)
    return render_template("update_user.html", user=user)

@app.route('/save_update', methods=['POST'])
def save_update():
    Peoples.update_user(request.form)
    return redirect(f'/show_user/{request.form["id"]}')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    Peoples.delete_user(id)
    return redirect('/')