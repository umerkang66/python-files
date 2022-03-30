from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='font-family: JetBrains Mono, sans-serif'>Hello, Umer Kang</h1>"

# $env:FLASK_APP = "hello" # tell flask which is the main server file
# then run "python -m flask run" or "flask run"
