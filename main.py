import os

def read_file_content(file_name):
    # Potentially vulnerable code
    file_path = os.path.join('/path/to/files', file_name)  # Fixed directory
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Simulating user input
user_input = input("Please enter file name: ")

# Potentially vulnerable code: using user input in a filesystem operation
file_content = read_file_content(user_input)
print(file_content)
