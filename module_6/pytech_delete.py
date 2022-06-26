# Christeen Safar 
# June 26, 2022
# Module 6.2 - pytech_delete.py
	

#import pymongo
from pymongo import MongoClient
	
url = "mongodb+srv://admin:admin>@cluster0.cl9pp.mongodb.net/?retryWrites=true&w=majority" 
client = MongoClient(url)
db = client.pytech
pytech = db.students
collection = db.Students

students = client.pytech.get_collection("students")

students_list = students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students_list:
    print("Student ID: {}".format(student["student_id"]))
    print("First Name: {}".format(student["first_name"]))
    print("Last Name: {}\n".format(student["last_name"]))

student_insert = { "student_id": 1010,
                    "first_name": "Jerry",
                    "last_name": "Jeferson"}
            
new_student_Id = students.insert_one(student_insert).inserted_id
print("-- INSERT STATEMENTS --")
print("Inserted student record {} {} into the students collection with document_id {}".format(student_insert["first_name"], student_insert["last_name"], new_student_Id))

students_list = students.find({})

print("-- DISPLAY NEW STUDENT LIST DOC --")
for student in students_list:
    print("Student ID: {}".format(student["student_id"]))
    print("First Name: {}".format(student["first_name"]))
    print("Last Name: {}\n".format(student["last_name"]))


students.delete_one({"student_id": 1010})

students_list = students.find({})

print("-- DELETED STUDENT ID: 1010 --")
for student in students_list:
    print("Student ID: {}".format(student["student_id"]))
    print("First Name: {}".format(student["first_name"]))
    print("Last Name: {}\n".format(student["last_name"]))


input("\n\nEnd of program, press any key to continue...")
