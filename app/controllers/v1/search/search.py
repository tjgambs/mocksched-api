
from flask import abort, Blueprint, jsonify
from app.utils import prepare_json_response
from app import db

from app.models.professors import Professors
from app.models.term_courses import TermCourses
from app.models.terms import Terms
from app.models.courses import Courses
from app.models.reviews import Reviews
import requests


mod = Blueprint("v1_search", __name__, url_prefix="/v1/search")


@mod.route("/all_terms", methods=["GET"])
def all_terms():
    q = (db.session.query(Terms)
         .order_by(Terms.stream))
    payload = [a.serialize for a in q.all()]
    data = {'results': payload}
    return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )


@mod.route("/all_subjects/<stream>", methods=["GET"])
def all_subjects(stream):
    sq = (db.session.query(TermCourses.course_id)
          .filter_by(stream=stream))
    q = (db.session.query(Courses.subject)
         .filter(Courses.id.in_(sq))
         .order_by(Courses.subject))
    payload = [{'subject': a.subject} for a in q.distinct()]
    data = {'results': payload}
    return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )


@mod.route("/by_subject_number/<subject>/<number>/<stream>", methods=["GET"])
def by_subject_and_number(subject, number, stream):
    sq = (db.session.query(TermCourses.course_id)
          .filter_by(stream=stream))
    q = (db.session.query(Courses)
         .filter(Courses.id.in_(sq)
                 & (Courses.subject.ilike(subject))
                 & (Courses.catalog_nbr.like(number + '%')))
         .order_by(Courses.catalog_nbr))
    payload = [a.serialize for a in q.all()]
    data = {'results': payload}
    return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )


@mod.route("/by_subject/<subject>/<stream>", methods=["GET"])
def by_subject(subject, stream):
    sq = (db.session.query(TermCourses.course_id)
          .filter_by(stream=stream))
    q = (db.session.query(Courses)
         .filter(Courses.id.in_(sq)
                 & (Courses.subject.ilike(subject)))
         .order_by(Courses.catalog_nbr))
    payload = [a.serialize for a in q.all()]
    data = {'results': payload}
    return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )


@mod.route("/by_number/<number>/<stream>", methods=["GET"])
def by_number(number, stream):
    sq = (db.session.query(TermCourses.course_id)
          .filter_by(stream=stream))
    q = (db.session.query(Courses)
         .filter(Courses.id.in_(sq)
                 & (Courses.catalog_nbr.like(number + '%')))
         .order_by(Courses.subject, Courses.catalog_nbr))
    payload = [a.serialize for a in q.all()]
    data = {'results': payload}
    return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )


@mod.route("/by_learning_domain/<learning_domain>/<stream>", methods=["GET"])
def by_learning_domain(learning_domain, stream):
    sq = (db.session.query(TermCourses.course_id)
          .filter_by(stream=stream))
    q = (db.session.query(Courses)
         .filter(Courses.id.in_(sq)
                 & (Courses.learning_domain == learning_domain))
         .order_by(Courses.subject, Courses.catalog_nbr))
    payload = [a.serialize for a in q.all()]
    data = {'results': payload}
    return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )


@mod.route("/by_learning_domain_subject/<learning_domain>/<subject>/<stream>", methods=["GET"])
def by_learning_domain_subject(learning_domain, subject, stream):
    sq = (db.session.query(TermCourses.course_id)
          .filter_by(stream=stream))
    q = (db.session.query(Courses)
         .filter(Courses.id.in_(sq)
                 & (Courses.learning_domain == learning_domain)
                 & (Courses.subject.ilike(subject)))
         .order_by(Courses.catalog_nbr))
    payload = [a.serialize for a in q.all()]
    data = {'results': payload}
    return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )


@mod.route("/by_learning_domain_number/<learning_domain>/<number>/<stream>", methods=["GET"])
def by_learning_domain_number(learning_domain, number, stream):
    sq = (db.session.query(TermCourses.course_id)
          .filter_by(stream=stream))
    q = (db.session.query(Courses)
         .filter(Courses.id.in_(sq)
                 & (Courses.learning_domain == learning_domain)
                 & (Courses.catalog_nbr.like(number + '%')))
         .order_by(Courses.subject, Courses.catalog_nbr))
    payload = [a.serialize for a in q.all()]
    data = {'results': payload}
    return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )


@mod.route("/by_learning_domain_subject_number/<learning_domain>/<subject>/<number>/<stream>", methods=["GET"])
def by_learning_domain_subject_number(learning_domain, subject, number, stream):
    sq = (db.session.query(TermCourses.course_id)
          .filter_by(stream=stream))
    q = (db.session.query(Courses)
         .filter(Courses.id.in_(sq)
                 & (Courses.learning_domain == learning_domain)
                 & (Courses.subject.ilike(subject))
                 & (Courses.catalog_nbr.like(number + '%')))
         .order_by(Courses.subject, Courses.catalog_nbr))
    payload = [a.serialize for a in q.all()]
    data = {'results': payload}
    return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )


@mod.route('/by_professor_id/<pid>')
def by_professor_id(pid):
    q = (db.session.query(Professors)
         .filter_by(id=pid).first())
    data = {'results': q.serialize if q else {}}
    return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )


@mod.route("/by_class/<subject>/<number>/<stream>", methods=["GET"])
def by_class(subject, number, stream):
    base_url = ('https://offices.depaul.edu/_layouts/DUC.SR.ClassSvc/DUClassSvc.ashx'
                '?action=getclasses&strm=%s&subject=%s&catalog_nbr=%s')
    url = base_url % (stream, subject.upper(), number)
    payload = requests.get(url).json()
    for p in payload:
        ratings = Professors.get_ratings(p['first_name'], p['last_name'])
        p.update(ratings)
    data = {'results': payload}
    return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )
