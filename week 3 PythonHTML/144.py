def multiply_nums(*args):
    multiply = 1
    # print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(2,3,4))
