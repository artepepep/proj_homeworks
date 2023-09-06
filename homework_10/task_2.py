with open("file.txt", 'r') as file:
    a = file.read()
a_upper = a.upper()
with open("file1.txt", 'w') as append_file:
    append_file.write(a_upper)