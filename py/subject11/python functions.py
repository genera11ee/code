
# Strings are similar to arrays
a = "Hello, Nico!"
print(a[1])
a = "Hello, Nico!"
print(len(a))

# Getting a substring
a = "Hello, You!"
print(a[7:10])

# Removing preceding and trailing whitespaces
a = "   Hello, You!   "
print(a.strip())

# Upper case and lower case
a = "Hello, You!"
print(a.lower())
print(a.upper())

# Replacing content inside a string
a = "This is a snowy day"
b = a.replace("snowy", "sunny")
print(b)

# Splitting a string into an array
words = "apples,oranges,bananas"
fruits = words.split(",")
print(fruits)

# Escape sequences
#New line:
# \n
#Tab:
# \t

# Finding a string within a string
a = "This is a great day to learn about programming."
b = a.find("great")
c = a.find("blue")
print(b) # b == 10
print(c) # c == -1

# String functions can be combined
a = "This is a great day to learn about programming."
b = a.replace("great", "beautiful").upper().split(" ")
print(b)