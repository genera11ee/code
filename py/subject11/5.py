text = "    Hello, You!    "

print(text[1])
print(len(text))

substring = text[7:10]
print(substring)

print(text)
stripped = text.strip()
print(stripped)

# message = input("Enter a message for Nico: ").strip()
# print(message.strip() + " Nico!")
# message = input("Enter a message for Nico: ").strip()
# print(message.strip() + " Nico!")

word = "KiWi"
print(word.upper())
print(word.lower())

text = "Hello Nico"
replaced = text.replace("Nico", "You")
print(replaced)

words = "Apples,Bananas,Oranges"
array = words.split(",")
print(array)
for word in array:
    print(word)

message = "\nHello \t You \nRascal"
print(message)
print(message.strip())

message = "Hello You, what is the weather like outside!"
result = message.find("weather")
print(result)
result = message.find("oranges")
print(result)
result = message.find("H")
print(result)

text = "     Hello You     "
print(text.strip().upper().replace("YOU", "NICO"))