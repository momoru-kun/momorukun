from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_babel import Babel

import logging

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

app = Flask(__name__)
app.config.from_object(Config)
app.logger.addHandler(stream_handler)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, async_mode=None)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

from app import routes, models
