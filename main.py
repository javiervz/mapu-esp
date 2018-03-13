#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from mapu_numbers import numbers_map_decimal, decimal_to_map_99, decimal_to_map_999, decimal_to_map_9999, decimal_to_map_99_esp, decimal_to_map_999_esp, decimal_to_map_9999_esp, map_esp

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/', methods=["POST"])
def transformed():
  text = request.form['text']
  #output = list()
  #words = text.split()
  output=map_esp(int(text))
  return render_template("results.html",
    output=output)

if __name__ == '__main__':
    app.run()
  

