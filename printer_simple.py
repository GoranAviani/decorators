def printer(func):
    def printer_simple(x, y):
        print("Function {} has received  values of {} and {}" .format(func.__name__, x, y))
        output = func(x, y)
        print("Output of the {}  function is {}".format(func.__name__, output))
        #return func(x, y) would run the some_function again, while this is not neccecary for this decorator
        #return func(x, y)
        #Return output returns the result of the somefunction to the main function
        return output
    return printer_simple

@printer
def some_function(var1, var2):
    #Some work is done here
    var3 = 5
    return var3

if __name__ == '__main__':
    result = some_function(1,2)
    test = result