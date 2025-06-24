from flask import Flask, render_template, request, flash, session
import random
import mysql.connector

app = Flask(__name__)
app.secret_key = 'Matlakala@574'

# Database connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Matlakala@574",
    database="trailor_system"
)
cursor = conn.cursor(dictionary=True)

@app.route('/')
def welcome():
    return render_template("index.html")
@app.route("/admin", methods=["GET"])
def admin():
    return render_template("admin.html")


# Ensure table exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS trailor_system (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        student_number VARCHAR(20),
        email_address VARCHAR(100) UNIQUE,
        password VARCHAR(255),
        account_type ENUM('user', 'admin')
    )
""")
conn.commit()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email_address = request.form['email_address']
        password = request.form['password']

        cursor.execute("""
            SELECT * FROM trailor_system
            WHERE email_address = %s AND account_type = 'user'
        """, (email_address,))
        user = cursor.fetchone()

        if user:
            if user['password'] == password:
                session['user_name'] = user['first_name']  # Optional: to show welcome on sensor pages

                # Redirect based on email
                if email_address == "T@edu.vut.ac.za":
                    return render_template("temperature_in.html", user=user['first_name'])
                

                elif email_address == "N@edu.vut.ac.za":
                    ldr_value = 70  # You can replace this with a dynamic value later
                    return render_template("LDR.html", ldr_value=ldr_value, user=user['first_name'])
                

                elif email_address == "S@edu.vut.ac.za":
                    return render_template("temperature_out.html", user=user['first_name'])
                
                elif email_address == "M@edu.vut.ac.za":
                    return render_template("infrared.html", user=user['first_name'])
                

                elif email_address == "P@edu.vut.ac.za":
                    return render_template("humidity.html", user=user['first_name'])
                
                else:
                    flash('You don’t have a sensor assigned under your name.', 'warning')
                    return render_template("login.html")
            else:
                flash('Incorrect password.', 'error')
                return render_template("login.html")
        else:
            flash('Incorrect email or not a user account.', 'error')
            return render_template("login.html")

    return render_template("login.html")

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        student_number = request.form['student_number']
        email_address = request.form['email_address']
        password = request.form['password']
        account_type= request.form['account_type']

        try:
            cursor.execute("""
                INSERT INTO trailor_system (first_name, last_name, student_number, email_address, password, account_type)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (first_name, last_name, student_number, email_address, password, account_type))
            conn.commit()
            flash("Signup successful!", "success")
            return render_template("admin.html")
        except mysql.connector.Error as err:
            flash(f"Error: {err}", "danger")
            return render_template("signup.html")
    else:
        return render_template("signup.html")


@app.route("/light")
def light():
    session.clear()

    cursor.execute("SELECT Timestamp, LDR FROM sensordata ORDER BY Timestamp DESC")
    data = cursor.fetchall()

    
    Timestamp = [row['Timestamp'] for row in data]
    H = [row['LDR'] for row in data]

    
    zip_data = zip(Timestamp,H)
    
    return render_template("LDR.html", zip_data=zip_data)

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')

# Global flag to track sensor state
sensor_enabled = False  

# Simulated IR sensor function
def read_ir_sensor():
    distance = round(random.uniform(20.0, 100.0), 2)
    status = "intruder" if distance <= 50 else "clear"
    return distance, status

@app.route('/motion', methods=['GET', 'POST'])
def motion():
    session.clear()

    cursor.execute("SELECT Timestamp, infrared FROM sensordata ORDER BY Timestamp DESC")
    data = cursor.fetchall()

    
    Timestamp = [row['Timestamp'] for row in data]
    H = [row['Infrared'] for row in data]

    
    zip_data = zip(Timestamp,H)
    
    return render_template("infrared.html", zip_data=zip_data)
@app.route('/humidity')
def humidity():
    session.clear()

    cursor.execute("SELECT Timestamp, Humidity FROM sensordata ORDER BY Timestamp DESC")
    data = cursor.fetchall()

    
    Timestamp = [row['Timestamp'] for row in data]
    H = [row['humidity'] for row in data]

    
    zip_data = zip(Timestamp,H)
    
    return render_template("humidity.html", zip_data=zip_data)

@app.route("/Temperature_in", methods=['GET'])
def temperature_in():
    session.clear()

    cursor.execute("SELECT Timestamp, Temperature_in FROM sensordata ORDER BY Timestamp DESC")
    data = cursor.fetchall()

    
    Timestamp = [row['Timestamp'] for row in data]
    H = [row['Temperature_in'] for row in data]

    
    zip_data = zip(Timestamp,H)
    
    return render_template("temperature_in.html", zip_data=zip_data)

@app.route("/Temperature_out", methods=['GET'])
def temperature_out():
    session.clear()

    cursor.execute("SELECT Timestamp, Temperature_out FROM sensordata ORDER BY Timestamp DESC")
    data = cursor.fetchall()

    
    Timestamp = [row['Timestamp'] for row in data]
    H = [row['Temperature_out'] for row in data]

    
    zip_data = zip(Timestamp,H)
    
    return render_template("temperature_out.html", zip_data=zip_data)

if __name__ == "__main__":
    app.run(debug=True)
