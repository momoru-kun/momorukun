from app import app, db
from flask import request
from app.models import vote

import datetime

@app.route('/vote', methods=["POST"])
def save_vote():
    now = datetime.datetime.now()
    v = vote.Vote(vote=request.form['vote'], time=now.strftime("%d-%m-%Y %H:%M"))
    db.session.add(v)
    db.session.commit()
    return 'ok'