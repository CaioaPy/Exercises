#Objective: Parse and manipulate JSON data.

#Instructions:

#Load a JSON string representing a collection of users with attributes like name, age, and email.
#Convert the JSON string into a Python dictionary.
#Extract and print the names and emails of users who are over 25 years old.
#Add a new user to the dictionary and convert it back to a JSON string.

import json

users = """
[
    { "name": "Master", "age": 24, "email": "example@email.com" },
    { "name": "Xiza", "age": 27, "email": "xiza@example.com" },
    { "name": "Play", "age": 31, "email": "play@example.com" }
]
"""

users = json.loads(users)

for user in users:
    print(user["email"])

newUser = { "name": "new", "age": 21, "email": "anew@example.com" }
users.append(newUser)

#indent == formating
updated_users_json = json.dumps(users, indent=3)
print("\nUpdated Users List in JSON format:")
print(updated_users_json)