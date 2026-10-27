with open('temp/constitution.txt') as file_object:
    text = file_object.read()

text_list = text.split('\n')
for line in text_list:
    print(line)