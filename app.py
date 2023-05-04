#!/usr/bin/python

from flask import Flask, render_template, request, redirect, url_for, flash
import csv


app = Flask(__name__)


@app.route('/')
def index():
    data = []
    usable_data = []
    with open("./data.csv", "r") as csvfile:
        for row in csvfile:
            data.append(row)

    for x in data:
        info = x.split(',')
        usable_data.append(info)

    return render_template("index.html", data=usable_data)


if __name__ == "__main__":
    app.run()
