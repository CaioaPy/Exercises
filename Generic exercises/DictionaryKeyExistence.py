#Create a function that takes a dictionary and a key, and returns True if the key exists in the dictionary, otherwise False.
#my code:

dictw = {
    "name" : "john",
    "age" : 12,
    "height" : "172cm",
    "mood" : "",
}

key = "age"

if key in dictw:
    print("the key exist in the dictionary")
else:
    print("the key does not exist in the dictionary")