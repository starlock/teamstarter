from flask.session import SessionMixin, SessionInterface
from flask import request
from datetime import datetime
import json
from uuid import uuid4
from db import sessions
from werkzeug.datastructures import CallbackDict

class PsqlSession(CallbackDict, SessionMixin):
    def __init__(self, initial=None, sid=None, new=False):
        print "psqlsession"
        def on_update(self):
            self.modified = True

        CallbackDict.__init__(self, initial, on_update)
        self.sid = sid
        self.new = new
        self.modified = False

class PsqlSessionInterface(SessionInterface):
    session_class = PsqlSession
    serializer = json

    def generate_sid(self):
        print "generate_sid"
        return str(uuid4())

    def open_session(self, app, request):
        sid = request.cookies.get(app.session_cookie_name)
        if not sid:
            sid = self.generate_sid()
            return self.session_class(sid=sid, new=True)

        val = sessions.select().where(
            sessions.c.session_id == sid
        ).execute().fetchone()
        if val is not None:
            # XXX either fetch only value or use a dict.
            data = self.serializer.loads(val[1])
            return self.session_class(data, sid=sid)

        return self.session_class(sid=sid, new=True)

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        if not session:
            sessions.delete().where(sessions.c.session_id == session.sid)

            if session.modified:
                response.delete_cookie(app.session_cookie_name, domain=domain)
            return

        cookie_exp = self.get_expiration_time(app, session)
        val = self.serializer.dumps(dict(session))

        if session.new:
            sessions.insert().execute(
                session_id = session.sid,
                value = val,
                created_at = datetime.now(),
                modified_at = datetime.now(),
                ip = request.remote_addr
            )
        else:
            sessions.update().where(
                sessions.c.session_id == session.sid
            ).values(
                value = val,
                modified_at = datetime.now()
            ).execute()

        response.set_cookie(app.session_cookie_name, session.sid,
                            expires=cookie_exp, httponly=True,
                            domain=domain)

