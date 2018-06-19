import decimal


def polynomial(n):
    return decimal.Decimal(n)**100


def exponential(n):
    return (decimal.Decimal(11)/decimal.Decimal(10))**n


def find_n():
    decimal.getcontext().prec = 28
    n_start = 10
    step = 1000
    n_end = n_start
    while polynomial(n_end) > exponential(n_end):
        n_end += step
    while n_end - n_start > 1:
        n = (n_end + n_start)/2
        if polynomial(n) < exponential(n):
            n_end = n
        else:
            n_start = n
    return n


if __name__ == '__main__':
    print find_n()
