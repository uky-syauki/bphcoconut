from flask import render_template, url_for

from app import app


@app.route("/")
def index():
	return render_template("blank.html")


@app.route("/login")
def login():
	return "Login View"
