def steps(n, count = 0):
    if n <= 0:
        raise ValueError("Only positive integers are allowed")
    return count if n == 1 else steps(n / 2 if n % 2 == 0 else n * 3 + 1, count + 1)