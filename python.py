def sum(x, y):
    return x + y


def mul(x, y):
    return x * y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Can't be divided by zero")
        return None


def sub(x, y):
    return x - y


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = sum(a, b)
sub = sub(a, b)
multi = mul(a, b)
div = div(a, b)

print(f"The sum of {a} + {b} is equal to {sum}")
print(f"The subtraction of {a} - {b} is equal to {sub}")
print(f"The multiplication of {a} * {b} is equal to {multi}")
print(f"The divison of {a} / {b} is equal to {div}")
