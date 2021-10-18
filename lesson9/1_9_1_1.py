
str_ = 'Hello file world!\n'

with open('myfile.txt', 'a+') as my_file:
    my_file.write(str_)
