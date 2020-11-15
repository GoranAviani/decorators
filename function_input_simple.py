def function_input(func):
    def print_input_type(user_input):
        try:
            val = int(user_input)
            print("Input is an integer number. Number = ", val)
        except ValueError:
            try:
                val = float(user_input)
                print("Input is a float  number. Number = ", val)
            except ValueError:
                print("No.. input is not a number. It's a string")
        return func(user_input)
    return print_input_type

@function_input
def test_function(user_input):
    print('This is test function with user input: {}' .format(user_input))


def main():
    user_input = input('input: ')
    test_function(user_input)
if __name__ == '__main__':
    main()