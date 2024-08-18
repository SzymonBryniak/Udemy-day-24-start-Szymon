import os
cwd = os.getcwd()
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     # file.close() # "with" automatically closes the file
path2 = r'C:\Users\Szymon Bryniak\Desktop\my_file.txt'
relative_path = '../../../Desktop/my_filerel.txt'
path_create = '../day-24-start-Szymon/pathcreate2.txt'
absolute_path = '/Users/Szymon Bryniak/Desktop/my_file.txt'
print(cwd)
with open(relative_path, mode="w") as file:
    file.write("\nNew text2")
    print(file.read())

