from DSApp import DSApp
from flask import render_template


@DSApp.route('/')
def home():
    return render_template('basic.html')


@DSApp.route('/linked_lists/')
def linked_lists():
    return render_template('LinkedLists.html')


@DSApp.route('/stacks/')
def stacks():
    return render_template('stacks.html')


@DSApp.route('/queues/')
def queues():
    return render_template('queues.html')


@DSApp.route('/trees/')
def trees():
    return render_template('trees.html')


@DSApp.route('/graphs/')
def graphs():
    return render_template('graphs.html')


@DSApp.route('/searching/')
def searching():
    return render_template('searching.html')


@DSApp.route('/sorting/')
def sorting():
    return render_template('sorting.html')


@DSApp.route('/hashing/')
def hashing():
    return render_template('hashing.html')