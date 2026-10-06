import os

import mariadb
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Erick"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The movie was good!"},
    ]
    return render_template("index.html", title="home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me {}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


@app.get("/db-check")
def db_check():
    conn = mariadb.connect(
        host=app.config["DB_HOST"],
        port=3306,
        user=app.config["DB_USER"],
        password=app.config["DB_PASSWORD"],
        database=app.config["DB_NAME"],
    )
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        return {"database_connected": cursor.fetchone()[0] == 1}
    finally:
        conn.close()
