def new_tips(argv):
    def tips(func):
        def nei(a, b):
            print('start %s %s' % (argv, func.__name__))
            func(a, b)
            print('stop')

        return nei
    return tips


@new_tips('add_module')
def add(a, b):
    print(a + b)


@new_tips('sub_module')
def sub(a, b):
    print(a - b)


add(5, 5)
sub(10, 3)
