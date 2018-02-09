# author: Molly Jacobsen
# This is a web app to give summaries of datasets

import scipy
import pandas
import sklearn
import numpy
import random
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)


@app.route("/data/iris")
def iris():
    header = "The iris"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    dataset = pandas.read_csv(url, names=names)
    rows = str(dataset.shape[0])
    columns = str(dataset.shape[1])
    return render_template('layout.html', **locals())


@app.route("/data/usersdata/", methods=['GET'])
def data():
    header = "Your"
    rows = "some"
    columns = "Some"
    return render_template('layout.html', **locals())


@app.route("/")
def basic():
    return ("Welcome to my website")


if __name__ == "__main__":
    app.run()
