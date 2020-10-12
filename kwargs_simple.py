
def checker_if_kwarg_none(func):
    def checker(**kwargs):
        for name, value in kwargs.items():
            if value == None:
                return None

        return func(**kwargs)
    return checker


@checker_if_kwarg_none
def some_function(**kwargs):
    var2 = kwargs['var2']
    return var2

def main():
    paramethers = {
     'var1': 1,
     'var2': 9999999
    }
    result = some_function(**paramethers)
    if result == None:
        print('One or more vars are empty')
    print(result)

    paramethers = {
        'var1': 1,
        'var2': None
    }
    result = some_function(**paramethers)
    if result == None:
        print('One or more vars are empty')
    print(result)

if __name__ == '__main__':
    main()