SQLITE = "sqlite:///project.db"
POSTGRES = 'postgresql+psycopg2://postgres:root@localhost:5432/blog_python'

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = POSTGRES

#    SQLALCHEMY_TRACK_MODIFICATIONS = False