import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "<MyFirstMDB>"
COLLECTION = "MyFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB:%s") % e

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter an option: ")
    return option

def get_record()
    print("")
    first = input("Enter First Name > ")
    last = input("Enter Last Name > ")

    try:
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
        except:
            print("Error Accessing the Database")

        if not doc:
            print("")
            print("Error! No results Found")

        return doc

def add_record():
    print("")
    first = input("Enter First Name >")
    last = input("Enter Last Name >")
    dob = input("Enter DOB >")
    gender = input("Enter Gender >")
    hair_colour = input("Enter Hair Colour >")
    occupation = input("Enter Occupation >")
    nationality = input("Enter Nationality >")

    new_doc = {'first:': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender,
                'hair_colour': hair_colour, 'occupation': occupation, 'nationality': nationality}


    try:
        coll.insert(new_doc)
        print("")
        print("Document Inserted")
    except:
        print("Error Accessing the Database")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
            print("")

conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

main_loop()