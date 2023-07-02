import os
from flask import render_template, current_app
from . import main
from . import item


@main.route("/")
def hello_world():
    current_app.logger.info("About to return Hello world")
    current_app.logger.debug("This is a debug statement")
    # the people dictionary should be served by the database
    # add an items list to the each person's entry in the people dictionary for their items
    d = item.Database(json_file=os.path.join(current_app.root_path, "main", "data.json"))
    d.load()
    print(d)
    print(d.persons)
    current_app.logger.info(current_app.root_path)
    return render_template("index.html", people=d.persons)


