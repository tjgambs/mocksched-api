from app.models.reviews import Reviews
from app import db


class Professors(db.Model):

    __tablename__ = "professors"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    overall_score = db.Column(db.DECIMAL(asdecimal=False))
    helpful_score = db.Column(db.DECIMAL(asdecimal=False))
    clarity_score = db.Column(db.DECIMAL(asdecimal=False))
    easy_score = db.Column(db.DECIMAL(asdecimal=False))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'overall_score': self.overall_score,
                'helpful_score': self.helpful_score,
                'clarity_score': self.clarity_score,
                'easy_score': self.easy_score,
                'reviews': self.reviews}

    @property
    def reviews(self):
        return [a.serialize for a in db.session.query(Reviews).filter_by(professor_id=self.id).all()]