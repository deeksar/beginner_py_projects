""" Enter your username and password in file 1, and you can see the result in file 2 without repetition.
username = ''
password = ''
"""
folder = 'C:\\Users\\alpha\\OneDrive\\vs_code\\python_project1\\'

file1 = 'Login.txt'
with open(file1, 'r') as file:
    content1 = file.read()

file2 = 'User_logined.txt'

# Split the content into lines and filter out duplicates
lines_to_write = []
existing_lines = set()

lines = content1.splitlines()
for i in range(0, len(lines), 2):
    if i + 1 < len(lines):
        first_line = lines[i].strip()
        second_line = lines[i + 1].strip()
        if first_line in existing_lines:
            continue
        else:
            lines_to_write.extend([first_line, second_line])
            existing_lines.add(first_line)

# Write the filtered lines to the User_logined.txt file
with open(file2, 'w') as file:
    for line in lines_to_write:
        file.write(line + '\n')

def check_lines(filename):
    existing_lines = set()

    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            if i + 1 < len(lines):
                first_line = lines[i].strip()
                second_line = lines[i + 1].strip()
                if first_line in existing_lines:
                    continue
                else:
                    existing_lines.add(first_line)
    print("printed check")
check_lines(file2)
