def result_printer(result):
    if result == None:
        print('One or more vars are empty')
    else:
        print(result)


def checker_if_kwarg_none(func):
    def checker(**kwargs):
        for name, value in kwargs.items():
            if value == None:
                return None

        return func(**kwargs)
    return checker


@checker_if_kwarg_none
def some_function(**kwargs):
    var1 = kwargs['var1']
    var2 = kwargs['var2']
    return 'ok', var1, var2

def main():
    paramethers = {
     'var1': 1,
     'var2': 9999999
    }
    result = some_function(**paramethers)
    result_printer(result)

    paramethers = {
        'var1': 1,
        'var2': None
    }
    result = some_function(**paramethers)
    result_printer(result)

if __name__ == '__main__':
    main()