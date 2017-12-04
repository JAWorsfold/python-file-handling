import os

for file in os.listdir('..'):
    if file != os.path.basename(os.getcwd()):
        # credit to 'bytesized' on stack overflow for his answer relating
        # to finding the 'basename' of the directory (rather than the path)
        # https://stackoverflow.com/questions/31258561/get-script-directory-name-python
        print(file)
