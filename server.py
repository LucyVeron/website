#!/usr/bin/python3

import os

from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
   return render_template('home.html', layout = "home")

@app.route('/gallery')
def get_gallery():
   gallery_image_names = os.listdir('./static/images/gallery')
   return render_template("gallery.html", layout = "gallery", gallery_image_names=gallery_image_names)

@app.route('/bio')
def get_bio():
   bio_image_names = os.listdir('./static/images/bio')
   return render_template("bio.html", layout = "bio", bio_image_names=bio_image_names)

if __name__ == '__index__':
   app.run(debug=True)
