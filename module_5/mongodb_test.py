# Christeen Safar 
# June 18, 2022
# Module 5.2 - mongodb_test

# Import MongoClient
import pymongo
from pymongo import MongoClient

# Create a variable named url and assign it the connection string value you copied from MongoDB Atlas
url = "mongodb+srv://admin:admin@cluster0.cl9pp.mongodb.net/?retryWrites=true&w=majority";

# Create a variable named client and call the MongoClient passing-in the url variable.
client = MongoClient(url)

# Create a variable named db and assign it to the pytech database instance.
db = client.pytech

# Get the students collection 
students = db.students

# Using Python’s built-in print statement, calling the list_collection_names method off of the db variable.
print("\n -- Pytech COllection List --")
print("\n ['students']")
print(db.list_collection_names())

# Exit message
input("\n\n  End of program, press any key to exit... ")
