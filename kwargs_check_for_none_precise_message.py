class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def result_printer(result):
    print('Variable {} has a value of None ({}).' .format(result['key_name'], result['result']))
    print(color.BOLD + color.RED +'Exit app..')


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