from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def detectPage():
    return render_template('index.html')