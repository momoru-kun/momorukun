from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    name = db.Column(db.String(255))
    color = db.Column(db.String(7))
    text = db.Column(db.Text)

    def __repr__(self):
        return "Message {}, time: {}".format(self.id, self.time)

