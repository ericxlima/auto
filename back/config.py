import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URI = os.environ.get('DATABASE_URI')
    if not DATABASE_URI:
        if not os.path.exists(os.path.join(basedir, 'app.db')):
            os.mknod(os.path.join(basedir, 'app.db'))
        DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


MEDIA_FOLDER = os.path.join(basedir, 'media')
