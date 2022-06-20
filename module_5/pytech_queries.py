# Christeen Safar 
# June 19, 2022
# Module 5.3 - pytech_queries.py

#import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin>@cluster0.cl9pp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# Students collection 
collection = db.Students

# find() Function:
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

 
# Students Data
for student in collection.find():
    print("Student ID:", student["student_id"])
    print("First Name:", student["first_name"])
    print("Last Name:", student["last_name"])
    print()
    
    
# Find_one()
print("\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
# One student with student id of 1008
student = collection.find_one({'student_id': "1008"})

# Print the information of the student id of 1008 
print("Student ID:", student["student_id"])
print("First Name:", student["first_name"])
print("Last Name:", student["last_name"])
print()

# Exit message
input("\n\n End of program, press any key to exit... ")
