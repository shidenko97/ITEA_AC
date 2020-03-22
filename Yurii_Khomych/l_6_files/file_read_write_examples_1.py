# f = open("text_file_name_1.txt", "w")
#
# f.write("Good")
# f.close()
# with open("text_file_name.txt", "r+") as file:
#     print(file.read())
#     print(file.read())
# print()
# file.read()
# try:
#     f = open("text_file_name_1.txt", "w")
#     f.write("Good")
#
# except , :
#
# finally:
#     f.close()

# with open("text_file_name.txt", "r+") as file:
#     print("This is the file name: ", file.name)
# line = file.read()
# print(line)
# line = file.read(24)
# line_data = file.readline()
# line_data = file.readlines()
# line_data = file.readlines(2)


# with open("text_file_name.txt", "r+") as file:
#     for line in file:
#         print(line)
#
# with open("text_file_name_2.txt", "w") as file:
#     file.write("This data is on line 5\n")

# with open("text_file_name_2.txt", "r+") as file:
#     file.write("This data is on line 9\n")
#     file.write("This data is on line 10\n")

# Append new values to file
# values = [1234, 5678, 9012]
#
# with open("text_file_name_3.txt", "a+") as file:
#     for value in values:
#         str_value = str(value)
#         file.write(str_value)
#         file.write("\n")
#

# # Read and write to file

# Open the file as read-only
# with open("text_file_name.txt", "r") as file:
#     file_contents = file.readlines()
#
# file_contents.insert(1, "This goes between line 1 and 2\n")
# file_contents = "".join(file_contents)
#
# # Re-open in write-only format to overwrite old file
# with open("text_file_name.txt", "w") as file:
#     file.write(file_contents)
#
# with open("text_file_name.txt", "r") as file:
#     for line in file:
#         print(line)

# with open("text_file_name.txt", "r") as file:
#     file_contents = file.readlines()
#     file_contents.insert(1, "This goes between line 1 and 2\n")
#     file_contents = "".join(file_contents)
#     file.write(file_contents)
#
# with open("text_file_name.txt", "r") as file:
#     for line in file:
#         print(line)

# import sys
# print(sys.argv)
# print(a)
# our_list = a.split(",")
# print(our_list)
# print("Fine")
#
# file_mode = sys.argv[1]
#
# with open("text_file_name.txt", file_mode) as file:
#     if file_mode == "r":
#
#     file_contents = file.readlines()
# file_contents.insert(1, "This goes between line 1 and 2\n")
# file_contents = "".join(file_contents)
# file.write(file_contents)
# print(file_contents)
#
# import os
# print(os.environ["TEST_VAR"])
# os.environ["YOUR_ENV"] = "SOME_VARIABLE"
# your_env = os.environ.get("YOUR_ENV")
# "xxx" * int(your_env)
# print(your_env)
#
