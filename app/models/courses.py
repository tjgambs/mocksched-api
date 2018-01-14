from app import db


class Courses(db.Model):

    __tablename__ = "courses"

    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    subject = db.Column(db.String)
    catalog_nbr = db.Column(db.String)
    acad_career = db.Column(db.String)
    description = db.Column(db.String)
    prerequisites = db.Column(db.String)
    learning_domain = db.Column(db.String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'title': self.title,
                'subject': self.subject,
                'catalog_nbr': self.catalog_nbr,
                'acad_career': self.acad_career,
                'description': self.description,
                'prerequisites': self.prerequisites,
                'learning_domain': self.learning_domain}
