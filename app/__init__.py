from config import Config

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

import os
import logging

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class = Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  db.init_app(app)
  migrate.init_app(app)

  from app.api import bp as api_bp
  app.register_blueprint(api_bp, url_prefix='/api')

  from app.auth import bp as auth_bp
  app.register_blueprint(auth_bp, url_prefix='/auth')

  from app.errors import bp as errors_bp
  app.register_blueprint(errors_bp)

  from app.main import bp as main_bp
  app.register_blueprint(main_bp)

  if not app.debug and not app.testing:
    if not os.path.exists('logs'):
      os.mkdir('logs')
    file_handler = RotatingFileHandler(f'logs/{Config.PROJECT}.log',
                                        maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info(f'{Config.PROJECT} startup')

  return app