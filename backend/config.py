class Config():
    DEBUG = False
    SQL_ALCHEMY_TRACK_MODIFICATIONS=False

class localDevelopmentCOnfig():
    SQLALCMEHY_DATABASE_URI = "sqlite:///database.sqlite3"