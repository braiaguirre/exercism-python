def square(n):
    if n not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (n - 1)
    
def total():
    return 2 ** 64 - 1