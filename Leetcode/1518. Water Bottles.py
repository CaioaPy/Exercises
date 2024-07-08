#There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

#The operation of drinking a full water bottle turns it into an empty bottle.

#Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

#Example 1:

#Input: numBottles = 9, numExchange = 3
#Output: 13
#Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
#Number of water bottles you can drink: 9 + 3 + 1 = 13.

def bottles_exchange(full_bottles, ex_bottles) -> int:
    total_bottles = 0
    total_bottles += full_bottles
    new_bottles = 0
    while full_bottles >= ex_bottles:
        if full_bottles - ex_bottles > 0:
            full_bottles = full_bottles - ex_bottles
            total_bottles += 1
            new_bottles += 1
            if new_bottles == ex_bottles:
                full_bottles += ex_bottles
                new_bottles = 0
        else:
            if full_bottles + new_bottles >= ex_bottles:
                total_bottles += 1
                full_bottles = full_bottles - ex_bottles
                new_bottles = 0
    return total_bottles
x = bottles_exchange(15, 4)
print(x)