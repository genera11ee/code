# import random

# for i in range(5):
#     print(random.randint(1,50))

# correct_answer = True
# if correct_answer:
#     print("That is correct")

number = input("Type a number: ")
try:
    result = int(number) + 1
except:
    print("Couldn't convert your input to a valid number")
    quit()
print("the result is " + str(result))
