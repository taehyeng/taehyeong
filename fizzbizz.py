def fizzbizzf(num):
    if (num % 3 == 0) & (num % 5 == 0):
        out = "FizzBizz"
    elif num % 3 == 0:
        out = "Fizz"
    elif num % 5 == 0:
        out = "Bizz"
    else:
        out = "ValueError"
    return out
