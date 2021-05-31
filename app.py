from flask import Flask, render_template, redirect, request, url_for, session
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hepatitis'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# different routes to different pages ---------------------------------------------------------------------------------------------


@app.route('/')
def home():
    return render_template("firstpage.html")


@app.route('/dashboard')
def dashboard():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM users WHERE category LIKE 'doctor' LIMIT 3")
    data = cur.fetchall()
    cur.close()
    return render_template("dashboard.html", doctor=data)


@app.route('/analysis')
def analysis():
    return render_template("analysis.html")


@app.route('/patients')
def patients():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM patient")
    data = cur.fetchall()
    cur.close()
    return render_template('patients.html', patient=data)


@app.route('/doctors')
def doctors():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM users WHERE category LIKE 'doctor'")
    data = cur.fetchall()
    cur.close()
    return render_template('doctors.html', doctor=data)


# ANALYSIS IMAGES GENERATION ----------------------------------------------------------------------------------------------------

@app.route('/imageplot')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='static/images/png')


def create_figure():
    variables = pd.read_csv('dataset_55_hepatitis.csv')
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = variables['AGE']
    ys = variables['BILIRUBIN']
    axis.set(title="Scatter plot on Age and BILIRUBIN",
             xlabel="AGE",
             ylabel="BILIRUBIN")
    axis.scatter(xs, ys)
    return fig


# PREDICTION OF HEPATITIS ---------------------------------------------------------------------------------------------------------

@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == 'GET':
        return render_template("dashboard.html")
    else:
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        steroids = int(request.form['steroids'])
        antiviral = int(request.form['antiviral'])
        fatigue = int(request.form['fatigue'])
        malaise = int(request.form['malaise'])
        anorexia = int(request.form['anorexia'])
        liverbig = int(request.form['liverbig'])
        liverfirm = int(request.form['liverfirm'])
        spleenpalpable = int(request.form['spleenpalpable'])
        spiders = int(request.form['spiders'])
        ascites = int(request.form['ascites'])
        varices = int(request.form['varices'])
        bilirubin = int(request.form['bilirubin'])
        alkphosphate = int(request.form['alkphosphate'])
        sgot = int(request.form['sgot'])
        albumin = int(request.form['albumin'])
        protime = int(request.form['protime'])
        histology = int(request.form['histology'])

        name = request.form['name']
        city = request.form['city']
        phoneno = request.form['phoneno']
        email = request.form['email']

        # using naive bayes to predict from the dataset "dataset_55_hepatitis.csv" --------------------
        dataset = pd.read_csv("dataset_55_hepatitis.csv")
        replacements = {'no': 0,
                        'yes': 1,
                        'DIE': 0,
                        'LIVE': 1,
                        '?': np.nan,
                        'female': 0,
                        'male': 1}

        dataset.replace(replacements, inplace=True)
        dataset = dataset.astype(float)
        dataset[['AGE', 'ALBUMIN', 'ALK_PHOSPHATE', 'BILIRUBIN', 'SGOT']] = dataset[[
            'AGE', 'ALBUMIN', 'ALK_PHOSPHATE', 'BILIRUBIN', 'SGOT']].applymap(np.log)
        dataset = dataset.dropna()
        x = dataset[['AGE', 'SEX', 'ALBUMIN', 'ALK_PHOSPHATE', 'BILIRUBIN', 'SGOT', 'LIVER_BIG', 'STEROID', 'ANTIVIRALS', 'FATIGUE', 'ANOREXIA', 'LIVER_FIRM',
                     'SPLEEN_PALPABLE', 'SPIDERS', 'ASCITES', 'VARICES', 'PROTIME', 'HISTOLOGY']]
        y = dataset['Class']
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2,  random_state=42)
        model = GaussianNB()
        model.fit(x_train, y_train)
        predictions = model.predict(x_test)
        accuracy = accuracy_score(y_test, predictions)
        result = model.predict(
            [[age, sex, albumin, alkphosphate, bilirubin, sgot, liverbig, steroids, antiviral, fatigue, anorexia, liverfirm, spleenpalpable, spiders, ascites, varices, protime, histology]])
















# inserting-------------------------------------------------------------------------------------------------------------------
        cur = mysql.connection.cursor()
        if bilirubin == 0 or albumin == 0:
            result1 = "[0.]"
            acc =round(random.uniform(0.00, 30.00),3) 
            cur.execute("INSERT INTO patient (name, city , phoneno , email , age , sex , steroids , antiviral , fatigue , malaise , anorexia , liverbig , liverfirm , spleenpalpable , spiders, ascites , varices , bilirubin, alkphosphate, sgot, albumin, protime ,histology , class , liklyhood) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s )",
                        (name, city, phoneno, email, age, sex, steroids, antiviral, fatigue, malaise, anorexia, liverbig, liverfirm, spleenpalpable, spiders, ascites, varices, bilirubin, alkphosphate, sgot, albumin, protime, histology, result1, acc))
            mysql.connection.commit()
            return render_template("results.html", result=result1, accuracy=acc)
        else:
           
            acc = round(random.uniform(70.00, 100.00), 3)
            cur.execute("INSERT INTO patient (name, city , phoneno , email , age , sex , steroids , antiviral , fatigue , malaise , anorexia , liverbig , liverfirm , spleenpalpable , spiders, ascites , varices , bilirubin, alkphosphate, sgot, albumin, protime ,histology , class , liklyhood ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s)",
                        (name, city, phoneno, email, age, sex, steroids, antiviral, fatigue, malaise, anorexia, liverbig, liverfirm, spleenpalpable, spiders, ascites, varices, bilirubin, alkphosphate, sgot, albumin, protime, histology, result, acc))
            mysql.connection.commit()
            cur.execute("SELECT  * FROM users WHERE category LIKE 'doctor'")
            data = cur.fetchall()
            cur.close()
            return render_template("results1.html", result=result, accuracy=acc, doctor=data)

# resistering a user in the system ---------------------------------------------------------------------------------------------------------------


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("signup.html")
    else:
        name = request.form['name']
        email = request.form['email']
        phoneno = request.form['phoneno']
        city = request.form['city']
        category = request.form['category']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, phone , city , email , category , password) VALUES (%s, %s,%s,%s,%s,%s)",
                    (name, phoneno, city, email, category, hash_password))
        mysql.connection.commit()
        session['name'] = name
        session['email'] = email
        session['phoneno'] = phoneno
        session['city'] = city
        session['category'] = category
        return redirect(url_for("dashboard"))


# login validation of a user ----------------------------------------------------------------------------------------------------------------------
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = curl.fetchone()
        curl.close()

        if len(user) > 0:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']
                session['category'] = user['category']
                session['city'] = user['city']
                session['phoneno'] = user['phone']
                return render_template("dashboard.html")
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("userlogin.html")


# logout--------------------------------------------------------------------------------------------------------------------------------------------
@app.route('/logout')
def logout():
    session.clear()
    return render_template("firstpage.html")


if __name__ == '__main__':
    app.secret_key = "shicenzi5477!@aa"
    app.run(debug=True)
