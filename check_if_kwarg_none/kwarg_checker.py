from check_if_kwarg_none.kwarg_checker_constants import (
    color,
    DECORATOR_NAME,
    ERROR_INTRO_MESSAGE
)



def failure_printer(result_paramether: dict):
    """
    Intention of this fun is to print when kwargs value is None.
    :param result: dict holding neccecary paramethers that need to be displayed to the user
    :return: n/a
    """
    print(color.RED + DECORATOR_NAME + ERROR_INTRO_MESSAGE + color.BOLD + result_paramether['function_name'] + color.END + color.RED + ' function has kwarg paramether {} with a value of {} .. (None).'
          .format(result_paramether['kwarg_key'], result_paramether['kwarg_value']))
    print(color.BOLD + color.RED + DECORATOR_NAME +'Stopping the program and exiting the decorator')


def check_if_kwarg_none(func):
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
                failure_printer({'kwarg_value': value, 'kwarg_key': name, 'function_name': function_name})
                exit()

        return func(**kwargs)
    return checker


