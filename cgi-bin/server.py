#!/usr/bin/python
import os, sys

sys.path.insert(0, '/home/majortom6/public_html/cgi-bin/myenv/lib/python2.6/site-packages')

from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
   return render_template('home.html', layout = "home")

@app.route('/about')
def about():
   return render_template('about.html', layout = "about")

@app.route('/gallery')
def get_gallery():
   gallery_image_names = os.listdir('./static/images/gallery')
   return render_template("gallery.html", layout = "gallery", gallery_image_names=gallery_image_names)

@app.route('/bio')
def get_bio():
   bio_image_names = os.listdir('./static/images/bio')
   return render_template("bio.html", layout = "bio", bio_image_names=bio_image_names)

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000,debug=True)
