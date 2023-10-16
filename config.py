import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

class Config(object):

  PROJECT = 'NAME OF THE PROJECT'

  HOST = os.environ.get('HOST')
  USER = os.environ.get('USER')
  PASSWORD = os.environ.get('PASSWORD')
  DATABASE = os.environ.get('DATABASE')
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SECRET_KEY = os.environ.get('SECRET_KEY')