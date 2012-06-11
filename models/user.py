import bcrypt
from datetime import datetime
from sqlalchemy.sql.expression import join
import db

from models import BaseModel
from models.project import Project

def is_correct_password(raw, hashed):
    """Check whether given raw password matches given hash."""
    return (hashed == bcrypt.hashpw(raw, hashed))

class User(BaseModel):

    properties = db.users.c.keys()

    def get_projects(self):
        data = join(db.user_projects, db.projects,
                db.user_projects.c.project_id == db.projects.c.id
            ).select(use_labels=True).where(
                db.user_projects.c.user_id == self.id
            ).execute()

        rows = data.fetchall()
        projects = []
        for row in rows:
            projects.append(Project.init(**row))

        return projects

    @classmethod
    def get(cls, id):
        data = db.users.select().where(db.users.c.id == id).execute()
        if data.rowcount == 0:
            return None
        row = data.fetchone()
        return cls.init(**row)

    @classmethod
    def modify(cls, id, bio):
        data = db.users.update().where(
                db.users.c.id == id
               ).values(
                bio = bio
               ).execute()
        if data.rowcount == 0:
            return None
        return cls.get(id)

    @classmethod
    def get_authenticated(cls, email, password):
        data = db.users.select().where(db.users.c.email == email).execute()
        if data.rowcount == 0:
            return None

        # Validate password
        row = data.fetchone()
        if not is_correct_password(password, row['password']):
            return None
        return cls.init(**row)

    @classmethod
    def create(cls, email, password):
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        created_at = modified_at = datetime.now()

        data = db.users.insert().execute(
            email = email,
            password = hashed,
            created_at = created_at,
            modified_at = modified_at,
        )
        id = data.inserted_primary_key
        return cls.init(id=id, email=email, password=password,
                        created_at=created_at, modified_at=modified_at)
