apples = 3
oranges = 5
fruits = apples + oranges

message = "There are " + str(fruits) + " fruits in the basket."
message2 = "There are "+ str(apples) + " apples in the basket."
print(message)
print(message2)

def add(a, b):
    result = a + b
    message3 = "The result is " + str(result) + "!"
    return message3

print(add(2,3))
