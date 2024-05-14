#Create a program that takes a list of numbers and returns a new list with unique elements of the first list.
#My code:
base_list = [12,323,13,21,53,21,43,243,243,432,21,243,21,243,4,21,43,12,53,432]
unique_list = []
for item in base_list:
    if item not in unique_list:
        unique_list.append(item)

print("complete list: ")
print(base_list)
print("unique elements in the list: ")
print(unique_list)
