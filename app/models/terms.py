from app import db


class Terms(db.Model):

    __tablename__ = "terms"

    id = db.Column(db.Integer, primary_key=True)
    stream = db.Column(db.String)
    description = db.Column(db.String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'stream': self.stream,
                'description': self.description
                }
