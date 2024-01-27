Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from flask import Flask, render_template, request, redirect, url_for, flash
import firebase_admin
from firebase_admin import auth, credentials

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['fullName']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']

        # Check if email or password is empty
        if not email:
            flash('Email is required.')
            return render_template('register.html')
        if not password:
            flash('Password is required.')
...             return render_template('register.html')
...         if len(password) < 6:
...             flash('Password must be >= 6 characters.')
...             return render_template('register.html')
...         if len(phone) < 10:
...             flash('Invalid number.')
...             return render_template('register.html')
... 
...         # Try to create a new user
...         try:
...             user = auth.create_user(
...                 email=email,
...                 password=password
...             )
...             flash('User created.')
...             return redirect(url_for('login'))
...         except Exception as e:
...             flash(f'Error: {e}')
...             return render_template('register.html')
...     else:
...         # Check if user is already logged in
...         if auth.current_user:
...             return redirect(url_for('main'))
...         return render_template('register.html')
... 
... @app.route('/login')
... def login():
...     # Redirect to login page
...     return render_template('login.html')
... 
... # Define the main route
... @app.route('/')
... def main():
...     # Redirect to main page
...     return render_template('main.html')
... 
... if __name__ == '__main__':
...     app.run(debug=True)
...  note
