# Christeen Safar 
# June 19, 2022
# Module 5.3 - pytech_insert.py

from pymongo import MongoClient
import certifi
import ssl
ca = certifi.where()

url = "mongodb+srv://admin:admin@cluster0.dli7w.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url,ssl=True,  ssl_ca_certs=ca)

db = client.pytech

John = {
    "student_id": "1007",
    "first_name": "John",
    "last_name": "James",}
 
Jane = {
    "student_id": "1008",
    "first_name": "Jane",
    "last_name": "Johnson",}

Jack = {
    "student_id": "1009",
    "first_name": "Jack",
    "last_name": "Jacob"}

students = db.students
 
print("\n  -- INSERT STATEMENTS --")
John_student_id = students.insert_one(John).inserted_id
print("  Inserted student record John James into the students collection with document_id " + str(John_student_id))

Jane_student_id = students.insert_one(Jane).inserted_id
print("  Inserted student record Jane Johnson into the students collection with document_id " + str(Jane_student_id))

Jack_student_id = students.insert_one(Jack).inserted_id
print("  Inserted student record Jack Jacob into the students collection with document_id " + str(Jack_student_id))

input("\n\n  End of program, press any key to exit... ")
