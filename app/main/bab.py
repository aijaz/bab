from flask import render_template, current_app
from . import main


@main.route("/")
def hello_world():
    current_app.logger.info("About to return Hello world")
    current_app.logger.debug("This is a debug statement")
    return render_template("index.html")
