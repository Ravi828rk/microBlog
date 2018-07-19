import os
# for database configuration
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # for secret key configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # for emailing errors
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['ravi828.rk@gmail.com']

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'flasktestingemail@gmail.com'
    MAIL_PASSWORD = 'flasktestingpassword'
    ADMINS = ['ravi828.rk@gmail.com']

    # for pagination
    POSTS_PER_PAGE = 10
