import pickle


class Person:
    def __init__(self):
        self.person_id = ''  # This identifier is guaranteed to be unique
        self.person_name = ''
        self.person_image_file = None

    def show_person(self):
        print(f"Person with id {self.person_id} and name {self.person_name}")
        if self.person_image_file:
            print(f"  The image file for this person is {self.person_image_file}")


class Item:
    def __init__(self):
        self.item_name = ''
        self.item_description = ''
        self.person_id = ''
        self.image_file = None

    def show_item(self):
        print(f"Item named {self.item_name}: {self.item_description}. Belonging to person with id {self.person_id}")
        if self.image_file is not None:
            print(f"  {self.image_file}")


class Database:
    def __init__(self, pickle_file):
        self.persons = []  # List of persons
        self.items = []  # List of items
        self.pickle_file = pickle_file

    def save(self):
        try:
            with open(self.pickle_file, "wb") as f:
                pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            print("Error during pickling object (Possibly unsupported):", ex)

    def add_person(self, person_id, person_name, person_image_file=None):
        # create a new Person object
        # assign the variable p to be that new Person object
        p = Person()

        # a newly-created person object has an empty string for person_id and person_name
        # set those attributes to what was passed in to this add_person method
        p.person_id = person_id
        p.person_name = person_name
        p.person_image_file = person_image_file

        # append this new object to our persons list
        self.persons.append(p)

    def add_item(self, item_name, item_description, person_id, image_file=None):
        # create a new Item object
        # assign the variable i to be that new Item object
        i = Item()

        # a newly-created item object has an empty string for item_name, item_description, and person_id
        # set those attributes to what was passed in to this add_item method
        i.item_name = item_name
        i.item_description = item_description
        i.image_file = image_file
        i.person_id = person_id

        # append this new object to our items list
        self.items.append(i)

    def load(self):
        try:
            with open(self.pickle_file, "rb") as f:
                # create a new database from the loaded file
                loaded_d = pickle.load(f)

                # copy persons and items from the loaded database to ourself
                self.persons = list(loaded_d.persons)
                self.items = list(loaded_d.items)
        except Exception as ex:
            print("Error during unpickling object (Possibly unsupported):", ex)

    def show(self):
        for person in self.persons:
            person.show_person()
        for item in self.items:
            item.show_item()


if __name__ == "__main__":
    d = Database()
    # d.add_person(1, 'Kayra')
    # d.add_person(2, 'Kdub')
    # d.show()
    # d.save()
    d.load()
    # d.show()
    # d.add_item(image_file="static/birbWithTheEarring.jpg", item_name="tablet", item_description="my new tablet", person_id=1123123)
    d.show()
    # d.save()
