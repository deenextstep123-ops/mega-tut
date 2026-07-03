# config file for keys which can
# then be used for encryption purposes
# and general storage of all config variables
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    