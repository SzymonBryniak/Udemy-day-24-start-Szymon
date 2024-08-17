# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     # file.close() # "with" automatically closes the file

with open("my_file2.txt", mode="w+") as file:
    file.write("\nNew text2")
