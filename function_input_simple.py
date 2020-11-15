def funtion_input(func):
    def print_input_type():

            return func()
    return print_input_type

@funtion_input
def test_function():
    print('This is test function!')


def main():
    test_function()
if __name__ == '__main__':
    main()