text_file = open("myfile.txt")

for line in text_file:
    print(line + "something")

text_file.close()

