#!/usr/bin/python3

import os

from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/gallery')
def get_gallery():
   image_names = os.listdir('./static/images/gallery')
   print(image_names)
   return render_template("gallery.html", image_names=image_names)

if __name__ == '__index__':
   app.run(debug=True)
