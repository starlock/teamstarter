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

def json_encode(row):
    obj = {}

    if row:
        keys = row.keys()
        for key in keys:
            if key not in blacklisted_keys:
                obj[key] = row[key]

    return json.dumps(obj, default=json_datetime_handler)
