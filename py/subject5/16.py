#else
secret_number = 5
guess = input("Guess the number between 1-10: ")

if secret_number != int(guess):
    print("You lose")
else:
    print("You win!")

print("Try to play again!")
