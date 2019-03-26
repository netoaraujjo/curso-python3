#!/usr/bin/python3
# implementacao recursiva


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    for fib in range(20):
        print(fibonacci(fib))
