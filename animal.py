from sys import argv

def cat():
    print('meow')

def default():
    print('hello')

def main():
    if len(argv) == 1:
        default()
    elif argv[1] == 'cat':
        cat()
    else:
        default()

if __name__ == '__main__':
    main()

