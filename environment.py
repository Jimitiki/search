import mathutils

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
    def __init__(self, marker):
        SIZE_INCREASE = 50
        vector = marker["orientation"]
        corners = marker["corners"]
        center = marker["center"]
        p1 = mathutils.move_point_away_from_point(corners[0], center, SIZE_INCREASE)
        p2 = mathutils.move_point_away_from_point(corners[1], center, SIZE_INCREASE)
        p3 = mathutils.move_point_away_from_point(corners[2], center, SIZE_INCREASE)
        p4 = mathutils.move_point_away_from_point(corners[3], center, SIZE_INCREASE)
        self.rect = (p1, p2, p3, p4)

    def get_rect(self):
        return self.rect

    #def intersects(self, rect):
    def intersects(self, line):
        return (mathutils.line_intersect_test(line[0], line[1], self.rect[0], self.rect[1])
                or mathutils.line_intersect_test(line[0], line[1], self.rect[1], self.rect[2])
                or mathutils.line_intersect_test(line[0], line[1], self.rect[2], self.rect[3])
                or mathutils.line_intersect_test(line[0], line[1], self.rect[3], self.rect[0]))

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

    def get_obstacles(self):
        return self.obstacles

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def intersects_obstacle_point(self, pos_x, pos_y):
        for obstacle in self.obstacles:
            if obstacle.contains(pos_x, pos_y):
                return True
        return False

    def intersects_obstacle(self, start_x, start_y, end_x, end_y):
        for obstacle in self.obstacles:
            if obstacle.intersects([(start_x, start_y), (end_x, end_y)]):
                return True
        return False        
