
from flask import abort, Blueprint, jsonify
from app.utils import prepare_json_response
from app import db

from app.models.professors import Professors
from app.models.courses import Courses
from app.models.reviews import Reviews


mod = Blueprint("v1_search", __name__, url_prefix="/v1/search")

@mod.route("/by_subject_and_number/<subject>/<number>", methods=["GET"])
def by_subject_and_number(subject,number):
	q = db.session.query(Courses).filter_by(subject=subject.upper(),catalog_nbr=number)
	payload = [a.serialize for a in q.all()]
	data = {'results': payload}
	return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    ) 

@mod.route("/by_subject/<subject>", methods=["GET"])
def by_subject(subject):
	q = db.session.query(Courses).filter(Courses.subject.ilike(subject))
	payload = [a.serialize for a in q.all()]
	data = {'results': payload}
	return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    ) 

@mod.route("/by_number/<number>", methods=["GET"])
def by_number(number):
	q = db.session.query(Courses).filter_by(catalog_nbr=number)
	payload = [a.serialize for a in q.all()]
	data = {'results': payload}
	return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )

@mod.route("/by_learning_domain/<learning_domain>", methods=["GET"])
def by_learning_domain(learning_domain):
	q = db.session.query(Courses).filter_by(learning_domain=learning_domain)
	payload = [a.serialize for a in q.all()]
	data = {'results': payload}
	return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    ) 

@mod.route("/by_professor_first/<first_name>", methods=["GET"])
def by_professor_first(first_name):
	q = db.session.query(Professors).filter(Professors.first_name.ilike(first_name))
	payload = [a.serialize for a in q.all()]
	data = {'results': payload}
	return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )

@mod.route("/by_professor_last/<last_name>", methods=["GET"])
def by_professor_last(last_name):
	q = db.session.query(Professors).filter(Professors.last_name.ilike(last_name))
	payload = [a.serialize for a in q.all()]
	data = {'results': payload}
	return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )

@mod.route("/by_professor_first_last/<first_name>/<last_name>/", methods=["GET"])
def by_professor_first_last(first_name,last_name):
	q = db.session.query(Professors).filter(Professors.first_name.ilike(first_name) & Professors.last_name.ilike(last_name))
	payload = [a.serialize for a in q.all()]
	data = {'results': payload}
	return jsonify(
        prepare_json_response(
            message="OK",
            success=True,
            data=data
        )
    )









