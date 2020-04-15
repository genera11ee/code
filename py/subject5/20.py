#chaining

first_number = input("Enter a number: ")
sec_number = input("Enter a second number: ")
result = float(first_number) - float(sec_number)

if result > 10:
    print("The result is greater than 10.")
elif result > 0:
    print("The result is greater than 0 but not than 10.")
elif result == 0:
    print("The result is 0.")
else:
    print("The result is a negative number")

print("You can try agian")