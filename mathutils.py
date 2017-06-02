import math

def normalize(x, y):
    m = magnitude(x, y)
    if (m == 0):
        return (0, 0)
    return (x / m, y / m)

def magnitude(x, y):
    return math.sqrt(x * x + y * y)

def dot_product(u, v):
    return u[0] * v[0] + u[1] * v[1]

def signed_angle(u, v):
    angle = math.acos(dot_product(u, v))
    sign = math.atan2(v[1], v[0]) - math.atan2(u[1], u[0])
    if sign < 0: sign += 2 * math.pi;
    sign -= math.pi

    if sign < 0: angle *= -1
    return angle

def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    print(dx, dy)
    return math.sqrt(dx * dx + dy * dy)
