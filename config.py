SQLITE = "sqlite:///project.db"
POSTGRES = 'postgresql+psycopg2://postgres:password@localhost:5432/blogpost_db'

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = POSTGRES