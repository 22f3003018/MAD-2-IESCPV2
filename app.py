from flask import Flask
from backend.config import localDevelopmentConfig

def createapp():
    app = Flask(__name__)

    app.config.from_object(localDevelopmentConfig)
    
    return app

app = createapp()

app.get('/')
def home():
    return "<h1>Home page</h1>"

if __name__ == "__main__":
    app.run()
