import time

def sleep(func):
    """
    Hardcoded sleep value and passin paramethers along the way, piggibacking them
    :param func:
    :return:
    """
    def sleep_now(**kwargs):
        time.sleep(3)
        return func(**kwargs)

    return sleep_now

@sleep
def calculate(**kwargs):
    var1 = kwargs['var1']
    var2 = kwargs['var2']
    return var2

if __name__ == '__main__':
    paramethers = {
     'var1': 1,
     'var2': 9999999
    }
    result = calculate(**paramethers)
    print(result)