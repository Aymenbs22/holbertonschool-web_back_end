#!/usr/bin/env python3
"""
Route module for the API
"""


from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


class BasicAuth(Auth):
