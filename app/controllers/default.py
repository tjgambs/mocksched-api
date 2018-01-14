#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify
from app.utils import prepare_json_response
from app import app

mod = Blueprint("default", __name__)


@mod.route("/", methods=["GET"])
def index():
    return jsonify(
        prepare_json_response(
            message="Don't know where to go? Query /help for more information.",
            success=True,
            data=None
        )
    )


@mod.route("/help", methods=["GET"])
def help():
    func_list = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != "static":
            methods = rule.methods
            methods.discard("OPTIONS")
            methods.discard("HEAD")
            func_list.append('%s -  %s' % (rule.rule, ' '.join(methods)))

    return jsonify(
        prepare_json_response(
            message="All URL endpoints",
            success=True,
            data=sorted(func_list)
        )
    )
