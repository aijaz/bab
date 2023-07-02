from item import Database
from item import Item
from item import Person

if __name__ == "__main__":
    d = Database(json_file="./data.json")
    # d.add_person(1, 'Kayra Çevik')
    # d.add_person(2, 'Mum')
    # d.add_person(3, 'Dad')
    # d.add_person(4, 'Birb', "/static/birbWithTheEarring.jpg")
    # d.add_item(image_file="static/cat.jpg", item_name="Pheephee", item_description="Pheephee does all the heavy lifting", person_id=4)
    d.load()
    d.show()
    # d.save()
    # Phydough - Fido
    # d.load()
    # # d.show()
    # # d.add_item(image_file="static/birbWithTheEarring.jpg", item_name="tablet", item_description="my new tablet", person_id=1123123)
    # d.show()
    # # d.save()
