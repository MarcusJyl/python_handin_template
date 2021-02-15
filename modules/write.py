def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as write_file:
        for item in lst:
            for element in item:
                write_file.write(str(element) + '\n')