def read_csv(input_file):
    with open(input_file) as file_object:
        content = file_object.readlines()
    data = []
    for line in content:
        data.append(line)

    print(data)