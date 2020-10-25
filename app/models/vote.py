from app import db

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vote = db.Column(db.Integer)
    time = db.Column(db.String(64))

    def __repr__(self):
        return '<Vote ID: {}; vote:{}>'.format(self.id, self.vote)