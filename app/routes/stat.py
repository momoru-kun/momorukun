from app import app, db
from app.models import Vote, Visit
from flask import render_template
import datetime

@app.route("/stats")
def statistics():
    votes = Vote.query.all()
    all_votes = []
    count = [0,0,0,0,0]
    for v in votes:
        d = {}
        d['time'] = v.time 
        d['id'] = v.id 
        d['vote'] = v.vote
        all_votes.append(d)
        if v.vote == 1:
            count[0] += 1
        elif v.vote == 2:
            count[1] += 1
        elif v.vote == 3:
            count[2] += 1
        elif v.vote == 4:
            count[3] += 1
        elif v.vote == 5:
            count[4] += 1

    now = datetime.datetime.now()
    visits = len(Visit.query.filter_by(time=now.strftime("%d-%m-%Y")).all())
    return render_template("stats.html", votes=votes, vote_cnt=count, visits=visits)