# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session, flash

# Add functions you need from databases.py to the next line!
from databases import add_student, get_tutor_by_username, auth_student, get_student_by_username
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
        return render_template("subjects_page.html", student =user )


@app.route('/login', methods=['GET', 'POST'])
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
            return render_template("log_in.html", error="Bad login")
    else:
        return render_template("log_in.html")
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
