from flask import session
from models.project import Project

def require_auth(f):
    def validate(*args, **kwargs):
        if 'user_id' not in session:
            return 'Unauthorized, not logged in', 403

        if 'user_id' in kwargs:
            if session['user_id'] != kwargs['user_id']:
                return 'Unauthorized, caught in the cookie jar', 403

        return f(*args, **kwargs)
    return validate

def require_project_owner(f):
    def validate(*args, **kwargs):
        if 'user_id' not in session:
            return 'Unauthorized, not logged in', 403

        if 'project_id' not in kwargs:
            return 'Unauthorized, unknown project', 403

        user_id = session['user_id']
        project_id = kwargs['project_id']
        has_access = Project.has_access(project_id, user_id)
        if not has_access:
            return 'Unauthorized, caught in the cookie jar', 403

        return f(*args, **kwargs)
    return validate

