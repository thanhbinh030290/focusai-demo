from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "FocusAI 2.0 is running successfully!"
