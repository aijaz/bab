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
    d = item.Database(pickle_file=os.path.join(current_app.root_path, "main", "data.pickle"))
    d.load()
    print(d)
    print(d.persons)
    current_app.logger.info(current_app.root_path)
    return render_template("index.html", people=d.persons)


@main.route("/setupDb")
def setup_db():
    d = item.Database(pickle_file=os.path.join(current_app.root_path, "main", "data.pickle"))
    d.add_person(1, 'Kayra Çevik')
    d.add_person(2, 'Mum')
    d.add_person(3, 'Dad')
    d.add_person(4, 'Birb', "/static/birbWithTheEarring.jpg")
    d.add_item(image_file="static/cat.jpg", item_name="Pheephee", item_description="Pheephee does all the heavy lifting", person_id=4)
    # d.load()
    # d.show()
    current_app.logger.debug(d.persons)
    d.save()
