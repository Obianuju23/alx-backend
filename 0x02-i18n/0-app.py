#!/usr/bin/env python3
"""A module that contains Flask app"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """function that returns html index for task 0"""
    return render_template('0-index.html')


if __name__ == '__main__':
    """this is main function"""
    app.run(host='0.0.0.0', port=5000, debug=True)
