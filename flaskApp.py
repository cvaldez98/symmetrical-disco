# my attempt at building my markov chain using flask
from flask import Flask, render_template, request
import markovfy
app = Flask(__name__)

class mchain(object):
    def __init__(self):
        self.markov = markovfy.markov()
    def yieldTweet(self):
        return self.markov.getText()

init = mchain()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("landing_page.html", tweet= init.yieldTweet())

@app.route('/getTweet', methods=['GET'])
def getTweet():
    print("Calling getTweet()")
    with app.test_request_context('/getTweet', method='GET'):
        return init.yieldTweet()


if __name__ == "__main__":
    app.run()
