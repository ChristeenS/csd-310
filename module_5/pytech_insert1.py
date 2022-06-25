# Christeen Safar 
# June 19, 2022
# Module 5.3 - pytech_insert.py

# Import MongoClient
from pymongo import MongoClient

# Set up connection
url = "mongodb+srv://admin:admin@cluster0.cl9pp.mongodb.net/?retryWrites=true&w=majority";

client = MongoClient(url)

db = client["pytech"]

pytech = db["students"]


# Students Data

John = {"student_id": "1007", "first_name": "John", "last_name": "James"}

Jane = {"student_id": "1008", "first_name": "Jane", "last_name": "Johnson"}

Jack = {"student_id": "1009", "first_name": "Jack", "last_name": "Jacob"}


students = [John, Jane, Jack]


# Insert Statement

print("- - INSERT STATEMENTS - -")

for student in students:
    student_id = pytech.insert_one(student).inserted_id
    print(f"Inserted student record {student['first_name']} {student['last_name']} into the students collection with document_id {student_id}")


# Exit message

print("\nEnd of program, press any key to exit...")
