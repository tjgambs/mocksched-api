from app import db


class Reviews(db.Model):

    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(
        db.Integer, db.ForeignKey('professors.id'), index=True)
    attendance = db.Column(db.String)
    clarity_color = db.Column(db.String)
    easy_color = db.Column(db.String)
    help_color = db.Column(db.String)
    help_count = db.Column(db.Integer)
    not_help_count = db.Column(db.Integer)
    online_class = db.Column(db.String)
    quality = db.Column(db.String)
    clarity = db.Column(db.Integer)
    course = db.Column(db.String)
    comments = db.Column(db.String)
    date = db.Column(db.Date)
    easy = db.Column(db.Integer)
    easy_string = db.Column(db.String)
    helpful = db.Column(db.Integer)
    interest = db.Column(db.String)
    overall = db.Column(db.DECIMAL(asdecimal=False))
    overall_string = db.Column(db.String)
    status = db.Column(db.Integer)
    text_book_use = db.Column(db.String)
    would_take_again = db.Column(db.String)
    sid = db.Column(db.Integer)
    taken_for_credit = db.Column(db.String)
    teacher = db.Column(db.String)
    teacher_grade = db.Column(db.String)
    teacher_rating_tags = db.Column(db.ARRAY(db.String))
    unuseful_grouping = db.Column(db.String)
    useful_grouping = db.Column(db.String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'professor_id': self.professor_id,
                'attendance': self.attendance,
                'clarity_color': self.clarity_color,
                'easy_color': self.easy_color,
                'help_color': self.help_color,
                'help_count': self.help_count,
                'not_help_count': self.not_help_count,
                'online_class': self.online_class,
                'quality': self.quality,
                'clarity': self.clarity,
                'course': self.course,
                'comments': self.comments,
                'date': self.date,
                'easy': self.easy,
                'easy_string': self.easy_string,
                'helpful': self.helpful,
                'interest': self.interest,
                'overall': self.overall,
                'overall_string': self.overall_string,
                'status': self.status,
                'text_book_use': self.text_book_use,
                'would_take_again': self.would_take_again,
                'sid': self.sid,
                'taken_for_credit': self.taken_for_credit,
                'teacher': self.teacher,
                'teacher_grade': self.teacher_grade,
                'teacher_rating_tags': self.teacher_rating_tags,
                'unuseful_grouping': self.unuseful_grouping,
                'useful_grouping': self.useful_grouping
                }
