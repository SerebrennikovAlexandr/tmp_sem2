# На 1000 г. мяса
#
# Поваренная соль 15 г


def calc_salt(m):
    try:
        m = int(m)
    except:
        m = 0

    return int(15 * m / 1000)


# A simple calculator
class Calculator:
    def __init__(self):
        pass

    def add(self, x1, x2):
        return x1 + x2

    def multiply(self, x1, x2):
        return x1 * x2

    def subtract(self, x1, x2):
        return x1 - x2

    def divide(self, x1, x2):
        if x2 != 0:
            return x1/x2
        return 'error'
