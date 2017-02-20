#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
   return render_template('hometest.html')

@app.route('/gallery.html')
def gallery():
   return render_template('gallerytest.html')

if __name__ == '__index__':
   app.run(debug=True)
