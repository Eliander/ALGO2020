with open('input.txt', 'r') as input_file:
    line = input_file.readline()
    output_file = open('output.txt', 'w')
    while line:
        output_file.write(line)
        line = input_file.readline()

input_file.close()
output_file.close()