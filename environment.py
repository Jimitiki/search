
class tag_obstacle:
    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

class environment:
    def __init__(self, start, goal):
        self.obstacles = []
        self.start = start
        self.goal = goal

    def get_start(self):
        return self.start

    def get_goal(self):
        return self.goal

    def add_obstacle(self, obsticle):
        self.obstacles += obsticle

    def intersects_obstacle_point(self, pos_x, pos_y):
        for obstacle in self.obstacles:
            if obstacle.contains(pos_x, pos_y):
                return True
        return False

    def intersects_obstacle(self, start_x, start_y, end_x, end_y):
        for obstacle in self.obstacles:
            if obstacle.intersects(start_x, start_y, end_x, end_y):
                return True
        return False
