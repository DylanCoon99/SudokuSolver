import sudoku
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return "<h1>This is my page</h1>"


if __name__ == "__main__":
    app.run(debug=True)