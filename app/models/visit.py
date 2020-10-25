from app import db

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(255))
    ip = db.Column(db.String(255))

    def __repr__(self):
        return "<Visit ip {}>".format(self.ip, self.time)