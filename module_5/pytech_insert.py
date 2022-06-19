# Christeen Safar 
# June 19, 2022
# Module 5.3 - pytech_insert.py

# Import MongoClient
from pymongo import MongoClient

# Set up connection
url = "mongodb+srv://admin:admin@cluster0.cl9pp.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

# Students data.
john = {
	"student_id":"1007",
	"first_name":"John",
	"last_name":"James",
	"enrollments": [
	{
		"term":"Spring",
		"gpa":"4.0",
		"start_date":"3/14/2022",
		"end_date":"5/16/2022",
		"courses":[
		{
			"course_id":"CSD 200",
			"description":"Foundation of Software Development",
			"instructor":"Professor Sampson",
			"grade":"A"
	    }
	    ]
    }
    ]
}

jane = {
	"student_id":"1008",
	"first_name":"Jane",
	"last_name":"Johnson",
	"enrollments": [
	{
		"term":"Summer",
		"gpa":"4.0",
		"start_date":"5/23/2022",
		"end_date":"7/24/2022",
		"courses":[
		{
			"course_id":"CSD 310",
			"description":"Database Development and Use",
			"instructor":"Professor Sampson",
			"grade":"A"
		}
		]
    }
    ]
}

jack = {
	"student_id":"1009",
	"first_name":"Jack",
	"last_name":"Jacob",
	"enrollments": [
	{
		"term":"Summer",
		"gpa":"4.0",
		"start_date":"3/14/2022",
		"end_date":"5/16/2022",
		"courses":[
		{
			"course_id":"CSD 320",
			"description":"Programming with Java",
			"instructor":"Professor Woods",
			"grade":"A"
		}
		]
    }
    ]
}

# Students collection 
students = db.students

# insert statements 
print("\n  -- INSERT STATEMENTS --")
john_student_id = students.insert_one(john).inserted_id
print(" Inserted student record John James into the students collection with document_id " + str(john_student_id))

jane_student_id = students.insert_one(jane).inserted_id
print(" Inserted student record Jane Johnson into the students collection with document_id " + str(jane_student_id))

jack_student_id = students.insert_one(jack).inserted_id
print(" Inserted student record Jack Jacob into the students collection with document_id " + str(jack_student_id))

# Exit message
input("\n\n  End of program, press any key to exit... ")
