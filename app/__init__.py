from flask import Flask
from main.bab_logging import setup_logging


def create_app():
    app = Flask(__name__)
    setup_logging(app)

    # attach blueprints here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

"""
https://example.com/hello
https://example.com/goodbye

https://example.com/users/find
https://example.com/users/delete
https://example.com/users/search

https://example.com/objects/test
https://example.com/objects/search
"""