def is_armstrong_number(n, r = 0):
    for d in str(n):
        r += int(d) ** len(str(n))
    return n == r
