SQLITE = "sqlite:///project.db"
POSTGRES = "posgresql+psycopg2://postgre:root@localhost:5432/Fix"

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = POSTGRES