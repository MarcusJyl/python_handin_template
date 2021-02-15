def print_file_content(file):
    with open(file) as file_object:
        content= file_object.readlines()
    
    for line in content:
        print(line.strip().split(','))


