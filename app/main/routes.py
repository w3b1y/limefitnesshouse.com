from app import db
from app.main import bp
from app.models import *

from flask import current_app, request, abort, render_template, redirect, url_for, jsonify

import sqlalchemy as sa

@bp.route('/', methods=['GET'])
def index():
  a = 50
  context = {'a': a}
  return render_template('index.html', context=context)


@bp.route('/prova2', methods=['GET'])
def index_1():
  a = 50
  context = {'a': a}
  return render_template('index.html', context=context)