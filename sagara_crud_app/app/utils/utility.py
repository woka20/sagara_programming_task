from flask import session
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return "Fail"
        return f(*args, **kwargs)
    return decorated_function