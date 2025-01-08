from my_project import app
from flask import Flask, render_template, redirect, url_for, flash, abort, request
from my_project.purchase_order.forms import LoginForm, RegistrationForm  # Import from the purchase_order folder
from my_project.models import User
from flask_sqlalchemy import SQLAlchemy
from my_project.models import db, login_manager
from flask_login import login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/home')  # New route for displaying the home page
def home():
    return render_template('home.html')


# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = None  # Ensure 'user' is initialized before use
    if form.validate_on_submit():  # If the form is submitted and validated
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()  # Get user by email
        
        if user and user.check_password(password):  # Check if the password matches
            login_user(user)
            flash("Logged in successfully!")
            next_url = request.args.get('next')  # Get next URL from the request
            if not next_url or not next_url.startswith('/'):  # Check for a valid 'next' URL
                next_url = url_for('welcome_user')
            return redirect(next_url)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash("Registration successful! You can now log in.", 'success')
        except IntegrityError:
            db.session.rollback()  # Revert any database changes
            flash("Username already exists. Please choose a different username.", 'error')
        return render_template('register.html', form=form)
    return render_template('register.html', form=form)


@app.route('/welcome_user')
@login_required
def welcome_user():
    return render_template('welcome_user.html')  # Corrected: added return statement


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out!")
    return redirect(url_for('home'))


# Route for dashboard (just for testing purposes)
@app.route('/dashboard')
@login_required
def dashboard():
    return "This is a protected dashboard page."


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
