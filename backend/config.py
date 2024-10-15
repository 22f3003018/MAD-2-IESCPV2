class Config():
    DEBUG = False
    SQL_ALCHEMY_TRACK_MODIFICATIONS=False

class localDevelopmentConfig(Config):
    SQLALCMEHY_DATABASE_URI = "sqlite:///database.sqlite3"
    DEBUG =True
    SECURITY_PASSWORD_HASH='bcrypt'
    SECURITY_PASSWORD_SALT='thisshouldbekeptsecret'
    SECRET_KEY="thisshouldbeasecret"

    WTF_CSRF_ENABLED=False

