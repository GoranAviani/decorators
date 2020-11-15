def funtion_input(func):
    def print_input_type(x, y):

            return func(x, y)
    return print_input_type

@funtion_input
def test_function(x, y):
    print('This is test function!')


def main():
    test_function()
if __name__ == '__main__':
    main()