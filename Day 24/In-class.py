# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
#
# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", "w") as file:
    file.write('My name is David Adeleke.')

with open("my_file.txt", "a") as file:
    file.write("\nI love playing tennis.")

with open("new_file.txt", "w") as file:
    file.write("New text")

# with open('/Users/DAVID/Desktop/new_file.txt') as file:     # Absolute File Path
#     contents = file.read()
#     print(contents)
#
# with open('../../../../../Desktop/new_file.txt') as file:   # Relative File Path
#     contents = file.read()
#     print(contents)

