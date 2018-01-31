import argparse

parser = argparse.ArgumentParser(description='Encrypt or decrypt based on a'
                                 ' given key.')
parser.add_argument('input', help='Input file.')
parser.add_argument('output', help='Output file.')
parser.add_argument('-k', '--key', type=str, metavar='', required=True,
                    help='The key to either encrypt or decrypt the file.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--decrypt', action='store_true',
                   help='Decrypt a file.')
group.add_argument('-e', '--encrypt', action='store_true',
                   help='Encrypt a file.')
args = parser.parse_args()

input_file_name = args.input
output_file_name = args.output
input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

key = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lst = [char for char in alphabet]
for char in [char for char in args.key.upper()]:
    if char not in key:
        key.append(char)
for char in alpha_lst[::-1]:
    if char not in key:
        key.append(char)

contents = input_file.read()
contents = [char.upper() for char in contents]
input_file.close()


if args.decrypt:
    for index, item in enumerate(contents):
        if item in key:
            key_index = key.index(item)
            contents[index] = alpha_lst[key_index]
        else:
            contents[index] = contents[index]

elif args.encrypt:
    for index, item in enumerate(contents):
        if item in key:
            alpha_index = alpha_lst.index(item)
            contents[index] = key[alpha_index]
        else:
            contents[index] = contents[index]

output_file.write(''.join(contents))
output_file.close()
