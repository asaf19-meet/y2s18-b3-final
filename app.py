# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session, flash

# Add functions you need from databases.py to the next line!
from databases import add_student, get_tutor_by_username, auth_student, get_student_by_username, auth_tutor, add_tutor


# Starting the flask app
app = Flask(__name__)
app.secret_key = "q34we;kHvWEJWE:KVNl"

# App routing code here
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('home.html')
    else:
        user = get_student_by_username(session["username"])
        return render_template("subjects_page.html", student = user )

# @app.route('/tutor/log_in')
# def log_in_tutor():
#     return render_template('log_in.html')
    
# @app.route('/student/log_in')
# def log_in_student():
# 	return render_template('log_in.html')
# @app.route('/tutor/sign_up')
# def sign_up_tutor():
# 	return render_template('sign_up.html')
# @app.route('/tutor')
# def tutor():
#     return render_template('tutor_page.html')

# @app.route('/student')
# def student():
#     return render_template('student_page.html')

@app.route('/tutor/student_request')
def student_request():
    return render_template('student_request_page.html')

@app.route('/student/subjects_page')
def subjects_page():
    student = get_student_by_username(session["username"])
    return render_template('subjects_page.html',student = student)

@app.route('/student/subjects_page/tutor_option')
def tutor_option():
    return render_template('tutor_option_page.html')


@app.route('/student/login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        student = auth_student(POST_USERNAME, POST_PASSWORD)
        
        if student is not None:
            session['logged_in'] = True
            session["username"] = student.username
            print("logged_in")
            return redirect(url_for('home'))
        else:
            print("wrong")
            return render_template("student_login.html", error="Bad login")
    else:
        return render_template("student_login.html")
 
@app.route("/student/logout")
def student_logout():
    session['logged_in'] = False
    return home()

@app.route('/tutor/login', methods=['GET', 'POST'])
def tutor_login():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        tutor = auth_tutor(POST_USERNAME, POST_PASSWORD)
        
        if tutor is not None:
            session['logged_in'] = True
            session["username"] = tutor.username
            print("logged_in")
            return redirect(url_for('home'))
        else:
            print("wrong")
            return render_template("tutor_login.html", error="Bad login")
    else:
        return render_template("tutor_login.html")
 
@app.route("/tutor/logout")
def tutor_logout():
    session['logged_in'] = False
    return home()

@app.route("/student/signup", methods=['GET', 'POST'])
def student_signup():
    if request.method == 'GET':
        return render_template('student_signup.html')
    else:
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        location = request.form['location']
        grade = request.form['grade']
        add_student(username,password,name,location,grade)
        return render_template('student_signup.html')
    

@app.route("/tutor/signup", methods=['GET', 'POST'])
def tutor_signup():
    if request.method == 'GET':
        return render_template('tutor_signup.html')
    else:
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        location = request.form['location']
        experience = request.form['experience']
        degree = request.form['degree']        
        add_tutor(username,password,name,location,experience,degree)
        return render_template('tutor_signup.html')






# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)



