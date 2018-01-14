from app import db
from app.models.courses import Courses


class TermCourses(db.Model):

    __tablename__ = "term_courses"

    stream = db.Column(db.String, primary_key=True)
    course_id = db.Column(db.String, primary_key=True)
