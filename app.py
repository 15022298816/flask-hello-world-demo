from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome to My Watchlist!</h1>'


@app.route('/hello')
def hello():
    return '<h1>Hello, Flask!</h1>'


if __name__ == '__main__':
    app.run(debug=True)