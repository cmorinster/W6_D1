from app import app
from flask import render_template
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/top5')
def top5():
    return render_template('top5.html')