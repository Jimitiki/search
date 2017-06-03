def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def point_in_polygon(pt, poly):
    result = False
    for i in range(len(poly)-1):
        if intersect((poly[i][0], poly[i][1]), ( poly[i+1][0], poly[i+1][1]), (pt[0], pt[1]), (float('inf'), pt[1])):
            result = not result
    if intersect((poly[-1][0], poly[-1][1]), (poly[0][0], poly[0][1]), (pt[0], pt[1]), (float('inf'), pt[1])):
        result = not result
    return result

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def poly_intersection(poly1, poly2):

    for i, p1_first_point in enumerate(poly1[:-1]):
        p1_second_point = poly1[i + 1]

        for j, p2_first_point in enumerate(poly2[:-1]):
            p2_second_point = poly2[j + 1]

            if line_intersection((p1_first_point, p1_second_point), (p2_first_point, p2_second_point)):
                return True

    return False

class tag_obstacle:
    def __init__(self, rect):
        self.rect = rect

    def intersects(self, rect):
        return poly_intersection(self.rect, rect)

    def contains(self, x, y):
        return point_in_polygon((x, y), self.rect)

class environment:
    def __init__(self, start, goal, height, width):
        self.obstacles = []
        self.start = start
        self.goal = goal
        self.height = height
        self.width = width

    def get_start(self):
        return self.start

    def get_goal(self):
        return self.goal

    def get_dimensions(self):
        return (self.width, self.height)

    def add_obstacle(self, obstacle):
        self.obstacles += obstacle

    def intersects_obstacle_point(self, pos_x, pos_y):
        for obstacle in self.obstacles:
            if obstacle.contains(pos_x, pos_y):
                return True
        return False

    def intersects_obstacle(self, start_x, start_y, end_x, end_y):
        rect = mathutils.build_rect_from_line((start_x, start_y), (end_x, end_y), 100)
        print(rect)
        for obstacle in self.obstacles:
            if obstacle.intersects(rect):
                return True
        return False
