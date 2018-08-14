# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session, flash

# Add functions you need from databases.py to the next line!
from databases import add_student, get_tutor_by_username, auth_student, get_student_by_username, auth_tutor, add_tutor, delete_all_tutors, delete_all_students, get_tutors, get_students


# Starting the flask app
app = Flask(__name__)
app.secret_key = "q34we;kHvWEJWE:KVNl"

# App routing code here
@app.route('/')
def home():
    if not session.get('logged_in_student'):
        return render_template('home.html')
    elif session.get('logged_in_student'):
        user_stu = get_student_by_username(session["username"])
        return render_template("subjects_page.html", student = user_stu)

    if not session.get('logged_in_tutor'):
        return render_template("home.html")
    elif session.get('logged_in_tutor'):
        user_tut = get_tutor_by_username(session["username"])
        return render_template("student_request.html", student = user_tut)

@app.route('/tutor/student_request')
def student_request():
    return render_template('student_request_page.html')

@app.route('/student/subjects_page')
def subjects_page():
    return render_template('subjects_page.html')

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
            session['logged_in_student'] = True
            session["username"] = student.username
            print("logged_in_student")
            return redirect(url_for('home'))
        else:
            print("wrong")
            return render_template("student_login.html", error="Bad login")
    else:
        return render_template("student_login.html")
 
@app.route("/student/logout")
def student_logout():
    session['logged_in_student'] = False
    return home()

@app.route('/tutor/login', methods=['GET', 'POST'])
def tutor_login():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        tutor = auth_tutor(POST_USERNAME, POST_PASSWORD)
        
        if tutor is not None:
            session['logged_in_tutor'] = True
            session["username"] = tutor.username
            print("logged_in_tutor")
            return redirect(url_for('home'))
        else:
            print("wrong")
            return render_template("tutor_login.html", error="Bad login")
    else:
        return render_template("tutor_login.html")
 
@app.route("/tutor/logout")
def tutor_logout():
    session['logged_in_tutor'] = False
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
        session['logged_in_student'] = True
        session["username"] = username
        return redirect(url_for('home'))
    

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
        session['logged_in_tutor'] = True
        session["username"] = username
        return redirect(url_for('home'))
        
# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)



