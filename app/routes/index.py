from flask import render_template, request
from app import app, db
from app.models import Visit, Message

import datetime

@app.route('/')
def index():
    try:
        v = Visit()
        now = datetime.datetime.now()
        v.time = now.strftime("%d-%m-%Y")
        v.ip = request.remote_addr
        db.session.add(v)
        db.session.commit()
    except:
        pass
    finally:
        return render_template('index.html', title="HelloWorld By MomoruKun", messages=Message.query.all())