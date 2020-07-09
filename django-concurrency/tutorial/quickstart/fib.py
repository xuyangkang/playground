def fib(x : int) -> int:
    if x == 0:
        return 1
    if x == 1:
        return 2
    return fib(x - 1) + fib(x - 2)
