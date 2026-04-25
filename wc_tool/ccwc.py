#Code to mimic the functionality of the wc UNIX tool

def open_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)

if __name__ == '__main__':
    open_file("test.txt")