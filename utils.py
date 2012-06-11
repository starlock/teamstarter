from flask import session

def auth_required(f):
    def validate(*args, **kwargs):
        if 'user_id' not in session:
            return 'Unauthorized, not logged in', 403

        if session['user_id'] != kwargs['user_id']:
            return 'Unauthorized, not your data', 403

        return f(*args, **kwargs)
    return validate

