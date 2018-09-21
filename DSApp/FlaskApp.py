from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('basic.html')


@app.route('/linked_lists/')
def linked_lists():
    return render_template('LinkedLists.html')


@app.route('/stacks/')
def stacks():
    return render_template('stacks.html')


@app.route('/queues/')
def queues():
    return render_template('queues.html')


@app.route('/trees/')
def trees():
    return render_template('trees.html')


@app.route('/graphs/')
def graphs():
    return render_template('graphs.html')


@app.route('/searching/')
def searching():
    return render_template('searching.html')


@app.route('/sorting/')
def sorting():
    return render_template('sorting.html')


@app.route('/hashing/')
def hashing():
    return render_template('hashing.html')


if __name__ == '__main__':
    app.run(debug=True)
