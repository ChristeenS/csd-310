# Christeen Safar 
# June 19, 2022
# Module 5.3 - pytech_insert.py

# Import MongoClient
from pymongo import MongoClient

# Set up connection
url = "mongodb+srv://admin:admin@cluster0.cl9pp.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

# Students collection 
collection = db.Students

# insert statements 
print("\n  -- INSERT STATEMENTS --")

# Students data.
student = {
    "student_id":"1007",
    "first_name":"John",
    "last_name":"James"
}

new_student_id = collection.insert_one(student).inserted_id
print(f"Inserted student record {student['first_name']} {student['last_name']} into the students collection with document_id {new_student_id}")

student = {
    "student_id":"1008",
    "first_name":"Jane",
    "last_name":"Johnson"
}

new_student_id = collection.insert_one(student).inserted_id
print(f"Inserted student record {student['first_name']} {student['last_name']} into the students collection with document_id {new_student_id}")

student = {
    "student_id":"1009",
    "first_name":"Jack",
    "last_name":"Jacob"
}

new_student_id = collection.insert_one(student).inserted_id
print(f"Inserted student record {student['first_name']} {student['last_name']} into the students collection with document_id {new_student_id}")

# Exit message
input("\n\n  End of program, press any key to exit... ")
