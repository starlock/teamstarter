from datetime import datetime
import db

from models import BaseModel

class Project(BaseModel):

    properties = db.projects.c.keys()

    @classmethod
    def all(cls):
        data = db.projects.select().execute()
        rows = data.fetchall()

        projects = []
        for row in rows:
            projects.append(cls.init(**row))
        return projects

    @classmethod
    def get(cls, id):
        data = db.projects.select().where(db.projects.c.id == id).execute()
        if data.rowcount == 0:
            return None
        row = data.fetchone()
        return cls.init(**row)

    @classmethod
    def modify(cls, id, name, description):
        data = db.projects.update().where(
                    db.projects.c.id == id
                ).values(
                    name = name,
                    description = description
                ).execute()
        if data.rowcount == 0:
            return None
        return cls.get(id)

    @classmethod
    def join(cls, project_id, user_id, role='MEMBER'):
        role = role.upper()

        created_at = modified_at = datetime.now()

        data = db.user_projects.insert().execute(
            user_id = user_id,
            project_id = project_id,
            role = role,
            created_at = created_at,
            modified_at = modified_at
        )

        return data.rowcount == 1

    @classmethod
    def create(cls, name, description, user_id):
        role = 'ADMIN'
        conn = db.engine.connect()
        trans = conn.begin()
        try:
            data = conn.execute(db.projects.insert(),
                name = name,
                description = description
            )

            [id] = data.inserted_primary_key

            created_at = modified_at = datetime.now()

            data = conn.execute(db.user_projects.insert(),
                user_id = user_id,
                project_id = id,
                role = role,
                created_at = created_at,
                modified_at = modified_at
            )

            trans.commit()
        except:
            trans.rollback()
            return None

        return cls.init(id=id, name=name, description=description,
                        user_id=user_id, modified_at=modified_at,
                        created_at=created_at)

    @classmethod
    def has_access(cls, project_id, user_id):
        data = db.user_projects.select() \
            .where(db.user_projects.c.user_id == user_id) \
            .where(db.user_projects.c.project_id == project_id) \
            .execute()
        if data.rowcount:
            return True
        return False
