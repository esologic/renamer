import os

count = 93

directory = os.fsencode(os.getcwd())

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".STL"):
        new_file_name = str.replace(filename, 'logo-assem - ', "3D" + str(count) + '_1_module-')
        os.rename(filename, new_file_name)
        count += 1
