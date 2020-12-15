def result_printer(result):
    print('Variable {} has a None value {}' .format(result['name'], result['result']))


def checker_if_kwarg_none(func):
    def checker(**kwargs):
        for name, value in kwargs.items():
            if value is None:
                result_printer({'result': None, 'key_name': name})
                exit()

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

    paramethers = {
        'var1': 1,
        'var2': None
    }
    result = some_function(**paramethers)

if __name__ == '__main__':
    main()