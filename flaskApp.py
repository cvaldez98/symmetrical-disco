# my attempt at building my markov chain using flask
from flask import Flask, render_template
from flask import request
import markovfy
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    text = markovfy.markov().getText()
    return render_template("landing_page.html", tweet=text)

if __name__ == "__main__":
    app.run()
