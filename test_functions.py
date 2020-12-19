from check_if_kwarg_none.kwarg_checker import check_if_kwarg_none

@check_if_kwarg_none
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