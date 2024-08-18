from flask import Blueprint, render_template, request, url_for, redirect, flash
from werkzeug.security import generate_password_hash
from .models import User
from blogr import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Data validation
        if not username:
            flash('Username is required', 'error')
            return render_template('auth/register.html')
        
        if not email:
            flash('Email is required', 'error')
            return render_template('auth/register.html')
        
        if not password:
            flash('Password is required', 'error')
            return render_template('auth/register.html')

        # Check if the email already exists
        user_email = User.query.filter_by(email=email).first()
        if user_email is not None:
            flash('Email is already registered', 'error')
            return render_template('auth/register.html')

        # Check if the username already exists
        user_username = User.query.filter_by(username=username).first()
        if user_username is not None:
            flash('Username is already taken', 'error')
            return render_template('auth/register.html')

        # Create a new user
        user = User(username=username, email=email, password=generate_password_hash(password))
        
        try:
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {e}', 'error')
            return render_template('auth/register.html')

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    # Implement login functionality here
    return render_template('auth/login.html')

@bp.route('/profile')
def profile():
    # Implement profile functionality here
    return render_template('auth/profile.html')
