from flask import session

def require_auth(f):
    def validate(*args, **kwargs):
        if 'user_id' not in session:
            return 'Unauthorized, not logged in', 403

        if 'user_id' in kwargs:
            if session['user_id'] != kwargs['user_id']:
                return 'Unauthorized, not your data', 403

        return f(*args, **kwargs)
    return validate

def require_project_owner(f):
    def validate(*args, **kwargs):
        if 'user_id' not in session:
            return 'Unauthorized, not logged in', 403

        if 'project_id' in kwargs:
            # TODO: Check if user have access to project when models are in place
            has_access = True
            if not has_access:
                return 'Unauthorized, not your data', 403

        return f(*args, **kwargs)
    return validate

