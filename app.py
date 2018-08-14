# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_student, get_all_students

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')
def checking():
	if 'username' in session:
		return"logged in as %s" % escape (session['username'])
	return "Not logged in"
@app.route("/student/login", methods = ["POST","GET"])
def slogin():

	if request.method == 'POST':
		a = request.form["username"]
		b = request.form["password"]
		session["username"] = a
		return redirect(url_for('checking'))
	else:
		return 

# @app.route("/tutor/login")	
# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
