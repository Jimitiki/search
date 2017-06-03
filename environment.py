
class tag_obstacle:
    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    def intersects(rect):
        return False

    def contains(x, y):
        return False

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
