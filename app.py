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

@app.route('/tutor')
def tutor():
    return render_template('tutor_page.html')

@app.route('/student')
def student():
    return render_template('student_page.html')

@app.route('/tutor/student_request')
def student_request():
    return render_template('student_request_page.html')

@app.route('/student/subjects_page')
def subjects_page():
    return render_template('subjects_page.html')

@app.route('/student/subjects_page/tutor_option')
def tutor_option():
    return render_template('tutor_option_page.html')

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
