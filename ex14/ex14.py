input_file_name = input("Input file name: ")
output_file_name = input("Output file name: ")
input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')
input_contents = input_file.readlines()
n = 1
for line in input_contents:
    output_file.write('/* ' + str(n) + ' */ ' + line)
    n += 1
input_file.close()
output_file.close()
