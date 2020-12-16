from check_if_kwarg_none.constants import (
    color,
    DECORATOR_NAME,
    ERROR_INTRO_MESSAGE
)



def failure_printer(result):
    print(color.RED + DECORATOR_NAME + ERROR_INTRO_MESSAGE +'Function: {} has kwarg paramether {} with a value of {} .. (None).'
          .format(result['function_name'], result['key_name'], result['result']))
    print(color.BOLD + color.RED + DECORATOR_NAME +'Stopping the program and exiting the decorator')


def checker_if_kwarg_none(func):
    """
    This decorator checks if any value of a given kwarg is None. If any is none decorator stops execution of the code
    and outputs the needed message.
    :param func:
    :return: If no kwarg values are not none: passing kwargs paramethers to a called function
    """
    function_name = func.__name__
    def checker(**kwargs):
        for name, value in kwargs.items():
            if value is None:
                failure_printer({'result': None, 'key_name': name, 'function_name': function_name})
                exit()

        return func(**kwargs)
    return checker


@checker_if_kwarg_none
def some_function(**kwargs):
    var1 = kwargs['var1']
    var2 = kwargs['var2']
    print(var2)
    return 'ok', var1, var2

def main():
    paramethers = {
     'var1': 1,
     'var2': 9999999
    }
    result = some_function(**paramethers)

    paramethers = {
        'var1': 1,
        'var2': None
    }
    result = some_function(**paramethers)

if __name__ == '__main__':
    main()