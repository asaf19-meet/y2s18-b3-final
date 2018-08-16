# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session, flash

#Jenny stuff
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# Add functions you need from databases.py to the next line!
from databases import *
import os


UPLOAD_FOLDER = '/path/to/the/uploads'
# Starting the flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "q34we;kHvWEJWE:KVNl"

# App routing code here
@app.route('/', methods=["POST", "GET"])
def home():
    if session.get('logged_in_student') == True:
        user_stu = get_student_by_username(session["username"])
        return render_template("subjects_page.html", student = user_stu)
    elif session.get('logged_in_tutor') == True:
        user_tut = get_tutor_by_username(session["username"])
        return render_template("tutor_page.html", tutor = user_tut)
    else:
        return render_template("home.html")



@app.route('/tutor/tutor_page')
def tutor_page():
    username = session["username"]
    tutor =get_tutor_by_username(username)
    return render_template('tutor_page.html', tutor = tutor)






@app.route('/student/subjects_page')
def subjects_page():
    if not session.get('logged_in_student'):
        return render_template('home.html')
    elif session.get('logged_in_student'):
        user_stu = get_student_by_username(session["username"])
        return render_template("subjects_page.html", student = user_stu)
    


@app.route('/student/subjects_page/tutor_option/<string:subject>', methods = ['GET','POST'])
def tutor_option(subject):
    user_stu = get_student_by_username(session["username"])
    if request.method == 'GET':
        return render_template('tutor_option_page.html',tutors = get_tutors_by_subject(subject), subject=subject)
    else: 
        tutor_username = request.form['requested_tutor']
        connections[subject](user_stu.username, tutor_username)
        return redirect(url_for('tutor_page',username = tutor_username))


@app.route('/student/login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        student = auth_student(POST_USERNAME, POST_PASSWORD)
        print(student)
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
        return redirect(url_for('student_signup'))
    else:
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        location = request.form['location']
        grade = request.form['grade']
        phone_number = request.form['phone_number']
        img = None
        if 'img' not in request.files:
            flash('No file part')
            return redirect(request.url)
        else:
            img = request.files['img'].read()  

        add_student(username,password,name,location,grade,phone_number, img)
        session['logged_in_student'] = True
        session["username"] = username


   
        # check if the post request has the file part
        
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

        subject_list = [request.form['biology'] if 'biology' in request.form else '', 
                        request.form['physics'] if 'physics' in request.form else '', 
                        request.form['math'] if 'math' in request.form else '']
        subject_string = ','.join(subject_list)
        print(subject_string)
        experience = request.form['experience']
        degree = request.form['degree']
        img, authentication = None, None
        if 'img' not in request.files:
            flash('No file part')
            return redirect(request.url)
        else:
            img = request.files['img'].read()
            authentication = request.files['authentication']
            print(authentication.filename)
            test_image = image.load_img(authentication, target_size = (64, 64))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            classifier = load_model('my_model.h5')
            result = classifier.predict(test_image)
            authen = None
            if (result[0][0])>=0.5:
                test_image = image.load_img('test_set/{}'.format(authentication), target_size = (64, 64))
                test_image = image.img_to_array(test_image)
                test_image = np.expand_dims(test_image, axis = 0)
                result = classifier.predict(test_image)
                
                prediction = 'Trueeeee'
                authen = True
                add_tutor(username,password,name,location,subject_string,experience,degree, img, authentication.read())
                session['logged_in_tutor'] = True
                session["username"] = username
                return redirect(url_for('tutor_page'))

            else:
                prediction = 'False'
                print (prediction)
                # add_tutor(username,password,name,location,subject_string,experience,degree, img, authentication.read())
                # session['logged_in_tutor'] = True
                # session["username"] = username
                return redirect(url_for('home'))
                           
                
        
# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)



