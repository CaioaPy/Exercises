#There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. 
#Every second, the person holding the pillow passes it to the next person standing in the line. 
#Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

#For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
#Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

#Example 1:

#Input: n = 4, time = 5
#Output: 2
#Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
#After five seconds, the 2nd person is holding the pillow.

n = 4
time = 5

def pass_the_pillow(person, time):
    i = 0
    persons = []
    while i <= person:
        persons.append(i)
        i += 1
    position = 1

    while time > 0:
        if position < person:
            position += 1
        elif position > person:
            position -= 1
        else:
            if position == 1:
                position += 1
            else:
                position -= 1
        time -= 1
    return position

x = pass_the_pillow(n, time)
print(x)