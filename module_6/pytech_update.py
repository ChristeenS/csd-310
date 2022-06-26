# Christeen Safar 
# June 26, 2022
# Module 6.2 - pytech_update.py
	

#import pymongo
from pymongo import MongoClient
	
url = "mongodb+srv://admin:admin>@cluster0.cl9pp.mongodb.net/?retryWrites=true&w=majority" 
client = MongoClient(url)
db = client.pytech
pytech = db.students
collection = db.Students

# Students Data
John = {
    "student_id": "1007", 
    "first_name": "John", 
    "last_name": "James"
    }
Jane = {
    "student_id": "1008", 
    "first_name": "Jane", 
    "last_name": "Johnson"
    }
Jack = {
    "student_id": "1009", 
    "first_name": "Jack", 
    "last_name": "Jacob"
    }



# Use the find() method to display all documents in the collection

Collection = students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in collection:
    print("Student ID: {}".format(student["student_id"]))
    print("First Name: {}".format(student["first_name"]))
    print("Last Name: {}\n".format(student["last_name"]))

result = students.update_one({"student_id": 1007}, {"$set": {"last_name": "James"}})

found_student = students.find_one({"student_id": 1007})

print("-- DISPLAYING STUDENT DOCUMENT FROM find one() QUERY --")
print("Student ID: {}".format(found_student["student_id"]))
print("First Name: {}".format(found_student["first_name"]))
print("Last Name: {}\n".format(found_student["last_name"]))

# Exit Message
input("\n\nEnd of program, press any key to continue...")


