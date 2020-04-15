def greet(name, age):
    message = "Your name is " + name + " and you are " + age + " years old."
    return message

name = input("Enter your name: ")
age = input("Enter your age: ")

print(greet(name, age))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

num_one = int(input("Enter a number: "))
num_two = int(input("Enter another number: "))

message = f"The result of {num_one} + {num_two} is {add(num_one, num_two)}"
print(message)

message = f"The result of {num_one} - {num_two} is {subtract(num_one, num_two)}"
print(message)

def get_result(answer):
    if answer == "a":
        return True
    else:
        return False

print("Do you like programing?")
print("a. Yes")
print("b. No")
result = input("Enter a or b: ")

if get_result(result):
    print("Awesome! Programming is really fun!")
else:
    print("Hang in there! It's an acquired taste!")

