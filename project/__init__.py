from flask import Flask
from flask_cors import CORS


def create_app():
    from . import routes
    app = Flask(__name__)
    CORS(app)
    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/shelter_files'
    app.config['UPLOAD_FOLDER'] = '/tmp'
    routes.init_app(app)
    # services.init_app(app)
    return app