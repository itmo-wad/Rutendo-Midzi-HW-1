from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("profile.html")

# @app.route('/styles')
# def index():
#     return render_template("profile.css")

app.run(host="localhost", port=5001, debug=True)