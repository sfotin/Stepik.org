file_name = input()
file = open(file_name, 'r')
content = file.read()
print(content)
file.close()
