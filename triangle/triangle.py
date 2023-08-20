def equilateral(sides):
    unique = set(sides)
    return check(sides) and len(unique) == 1

def isosceles(sides):
    unique = set(sides)
    return check(sides) and len(unique) == 2 or len(unique) == 1

def scalene(sides):
    unique = set(sides)
    return check(sides) and len(unique) == 3

def check(sides):
    a, b, c = sides;
    return a + b >= c and b + c >= a and c + a >= b and a > 0 and b > 0 and c > 0;
