#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Run the python server
    - host: localhost
    - port: 5000
    - debug: True
"""
from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
