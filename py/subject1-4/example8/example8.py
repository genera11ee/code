def add(number_one, number_two):
    result = number_one + number_two
    return result

def subtract(number_one, number_two):
    result = number_two - number_one
    return result
    
def multiply(number_one, number_two, number_three):
    return number_one * number_two * number_three


total = add(3,7)
print(total)

subtraction = subtract(3,7)
print(subtraction)

multiplication = multiply(1,2,3)
print(multiply(1,2,3))

def message(name):
    return "Hello " + name

print(message("Rick"))
