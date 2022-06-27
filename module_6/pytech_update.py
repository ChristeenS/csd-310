# Christeen Safar 
# June 26, 2022
# Module 6.2 - pytech_update.py



from pymongo import MongoClient

url = "mongodb+srv://admin:admin>@cluster0.cl9pp.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
    
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Joy"}})

John = students.find_one({"student_id": "1007"})

print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

print("  Student ID: " + John["student_id"] + "\n  First Name: " + John["first_name"] + "\n  Last Name: " + John["last_name"] + "\n")

#Exit Message
input("\n\n  End of program, press any key to continue...")
