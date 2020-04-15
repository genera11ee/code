secret_number = 8
secret_color = "green"

def guess(number, color):
    if int(number) == secret_number and color == secret_color:
        return "You've found both the secret number and the secret color!"
    elif int(number) == secret_number or color == secret_color:
        return "You found at least one of the secrets!"
    else:
        msg_1 = "You didn't find any of the secrets!"
        msg_2 = "Better luck next time!"
        return msg_1 + " " + msg_2

print(guess(input("Enter a number 1-10: "), input("Enter a color: ")))
print("Try again?")