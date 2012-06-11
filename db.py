from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import json

DATABASE_URI = 'postgresql://webadmin@/teamstarter'

engine = create_engine(DATABASE_URI, convert_unicode=True)
metadata = MetaData(bind=engine)

users = Table('users', metadata, autoload=True)
sessions = Table('sessions', metadata, autoload=True)
projects = Table('projects', metadata, autoload=True)
user_projects = Table('user_project_rel', metadata, autoload=True)

blacklisted_keys = ( 'password', )

def json_datetime_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return None

def blacklist_stripper(obj):
    keys = obj.keys()
    for key in keys:
        for blacklist in blacklisted_keys:
            if blacklist in key:
                del obj[key]

def json_encode(obj):
    # Temporary hack until better fix arrives
    if type(obj) == list:
        for key, value in enumerate(obj):
            if type(obj[key]) == dict:
                blacklist_stripper(obj[key])
    elif type(obj) == dict:
        blacklist_stripper(obj)

    return json.dumps(obj, default=json_datetime_handler)
