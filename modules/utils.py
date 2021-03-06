import os

def get_file_name(folderpath, out):
    entries = os.listdir(folderpath)
    with open(out, 'w') as file_object:
        for item in entries:
            file_object.write(item + '\n')


def get_all_file_names(folderpath, out):
    with open(out, 'w') as file_writer:
        for root, dirs, files in os.walk(folderpath, topdown='True'):
            for name in files:
                file_writer.write(name + '\n')


def print_line_one(file_names):
    for file in file_names:
        with open(file, 'r') as file_object:
                print(file_object.readlines(1))
            

def print_emails(file_names):
    for file in file_names:
        with open(file, 'r') as file_object:
            lines = file_object.readlines()
            for line in lines:
                if line.__contains__('@'): print(line + '\n')
            
def write_headlines(md_files, out):
    lines = []
    for file in md_files:
        with open(file) as read_file:
            lines.append(read_file.readlines())
    with open(out, 'w') as write_file:
        for line in lines:
            for thing in line:
                if thing.__contains__('#'):
                   
                    write_file.write(thing)
     