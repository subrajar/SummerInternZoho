from flask import Flask

app = Flask(__name__)


@app.route('/')
def hii():
    return "hello"


@app.route('/customer')
def get_customer():
    return {"cust1": "subraja"}
