import sys


def print_file_content(file):
    with open(file) as file_object:
        content= file_object.readlines()
    
    for line in content:
        print(line.strip().split(','))


def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as write_file:
        for item in lst:
            for element in item:
                write_file.write(str(element) + '\n')


def read_csv(input_file):
    with open(input_file) as file_object:
        data = []
        for line in file_object:
            data.append(line.split(','))
    return data
    
if __name__ == '__main__':
    args = sys.argv
    input = args[len(args) -1]
    lis = read_csv(input)

    if(args.__contains__("--file")):
       
        file = args[args.index("--file") +1]
        write_list_to_file(file, lis)
    else:
        print(lis)
