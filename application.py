from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello from Azure Web App! -V3.0 dev file change</h1>"
