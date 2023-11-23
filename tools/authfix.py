import os
import fileinput


def replace_in_files(directory):
    file_extension = ".py"
    old_string = "auth_settings = []  # noqa: E501"
    new_string = "auth_settings = ['Authorization']"
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                replace_in_file(file_path, old_string, new_string)


def replace_in_file(file_path, old_string, new_string):
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            print(line.replace(old_string, new_string), end='')


def replace_multiline_in_file(file_path, old_multiline, new_multiline):
    with open(file_path, 'r') as file:
        content = file.read()

    with open(file_path, 'w') as file:
        file.write(content.replace(old_multiline, new_multiline))


replace_in_files('src/cudo_compute')

with open('tools/func.txt', 'r') as replacement_file:
    new_func = replacement_file.read()

with open('tools/old_func.txt', 'r') as find_file:
    old_func = find_file.read()

replace_multiline_in_file('src/cudo_compute/configuration.py', old_func, new_func)
