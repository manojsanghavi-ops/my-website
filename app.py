import os
from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/cybersecurity")
def cybersecurity():
    return render_template("cybersecurity.html")

@app.route("/cybersecurity")
def cybersecurity():
    return render_template("cybersecurity.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == os.environ.get("LOGIN_PASSWORD"):
            return render_template("success.html")

        return "Invalid username or password"

    return render_template("login.html")
if __name__== "__main__":
    app.run(port=5000)
