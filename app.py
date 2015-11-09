from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")
  
@app.route('/add_const.html')
def add_agency():
  return render_template("add_agency.html")
  
@app.route('/add_board.html')
def add_board():
  return render_template("add_board.html")

#why is this routing to the agency?
@app.route('/add_const.html')
def add_const():
  return render_template("add_const.html")

@app.route('/add_donor.html')
def add_donor():
  return render_template("add_donor.html")
  
@app.route('/add_member.html')
def add_member():
  return render_template("add_member.html")

@app.route('/add_staff.html')
def add_staff():
  return render_template("add_staff.html")
  
@app.route('/add_vendor.html')
def add_vendor():
  return render_template("add_vendor.html")
  
app.run(debug=True)