from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('basic.html')


@app.route('/linkedlists/')
def linkedlists():
    return render_template('LinkedLists.html')


if __name__ == '__main__':
    app.run(debug=True)
