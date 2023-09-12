from flask import Blueprint, jsonify, render_template, redirect, url_for, flash, request, session
from app.utils.utility import login_required
from app import db, bcrypt
from app.user.model import User


auth = Blueprint('user', __name__)
    


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Create a new user
        new_user = User(username=username, password=password, name=name, email=email)

        try:
            # Add the user to the database and commit the transaction
            db.session.add(new_user)
            db.session.commit()
            
        except Exception as e:
            # Handle registration failure (e.g., username already exists)
            db.session.rollback()
            return 'Registration failed: ' + str(e)

    return 'Registration successful!'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Create a new user
        user = User.query.filter_by(username=username).first()
        hashed=user.set_password(password)
        if user and user.check_password(password):
            session["user_id"]=username
            return 'Login successful!'
    return 'Login failed'        


   

@auth.route('/profile', methods=['GET'])
@login_required
def profile():
    users = User.query.all()
    users_data = [user.as_dict() for user in users]
    if users is not None:   
        return jsonify(users_data)
    return "Not Found"
    

@auth.route('/profile/<int:user_id>', methods=['GET'])
@login_required
def profile_id(user_id):
    users = User.query.get(user_id)
    if users is not None:    
       return users.as_dict()
    return "Not Found"


@auth.route('/update_profile/<int:user_id>', methods=['PUT'])
@login_required
def update_profile(user_id):
    usr=User.query.get(user_id)
    
    if 'username' in request.form:
        usr.username = request.form['username']
    if 'name' in request.form:
        usr.name = request.form['name']
    if 'email' in request.form:
        usr.email = request.form['email']
    if 'password' in request.form:
        usr.password = request.form['password']


    try:
            # Add the user to the database and commit the transaction
            db.session.add(usr)
            db.session.commit()
            
    except Exception as e:
            # Handle registration failure (e.g., username already exists)
            db.session.rollback()
            return 'Update failed: ' + str(e)
        
    
    return 'Update success', 200    

@auth.route('/logout')
@login_required
def logout():
    session.pop("user_id", None)
    return "Logout Sucess"