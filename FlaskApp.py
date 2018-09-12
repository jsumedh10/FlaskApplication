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


if __name__ == '__main__':
    app.run(debug=True)
