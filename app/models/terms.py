from app import db


class Terms(db.Model):

    __tablename__ = "terms"

    stream = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'stream': self.stream,
                'description': self.description}
