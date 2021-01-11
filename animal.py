from sys import argv

<<<<<<< HEAD
def cat():
    """
    docstring for cat
    """
    print('meow')

=======
>>>>>>> 767e0f4 (animal: added dog logic)
def default():
    print('hello')

def dog():
    print('bark')
    print('woof')

def main():
<<<<<<< HEAD
    if len(argv) == 1:
        default()
    elif argv[1] == 'cat':
        cat()
=======
    if len(argv) < 2:
        default()
    elif argv[1] == 'dog':
        dog()
>>>>>>> 767e0f4 (animal: added dog logic)
    else:
        default()

if __name__ == '__main__':
    main()

