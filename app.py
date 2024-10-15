from flask import Flask
from backend.config import localDevelopmentConfig
from backend.models import db,User,Role
from flask_security import Security,SQLAlchemySessionUserDatastore

def createapp():
    app = Flask(__name__)

    app.config.from_object(localDevelopmentConfig)
    
    db.init_app(app)


    #flask security
    datastore= SQLAlchemySessionUserDatastore(db,User,Role)
    app.security = Security(app,datastore=datastore)
    app.app_context().push()

    return app

app = createapp()

app.get('/')
def home():
    return "<h1>Home page</h1>"

if __name__ == "__main__":
    app.run()
