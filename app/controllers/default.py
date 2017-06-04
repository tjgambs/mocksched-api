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
    """
    Returns a list of available URLs.
    :returns: A JSON response object
    :rtype: flask.Response
    """
    # func_list = {}
    func_list = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != "static":
            methods = rule.methods
            methods.discard("OPTIONS")
            methods.discard("HEAD")
            func_list.append(rule.rule + "  -  " + repr(methods).replace("set(","").replace(")",""))

    return jsonify(
        prepare_json_response(
            message="All URL endpoints",
            success=True,
            data=sorted(func_list)
        )
    )
