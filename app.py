from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")
  
@app.route('/add_const.html')
def add_const():
  return render_template("add_const.html")
  
@app.route('/')
def main_template():
  return render_template("main_template.html")

app.run(debug=True)