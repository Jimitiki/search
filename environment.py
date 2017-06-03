
class tag_obsticle:
    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

class environment:
    def __init__(self, start, goal):
        self.obsticles = []
        self.start = start
        self.goal = goal

    def get_start(self):
        return self.start

    def get_goal(self):
        return self.goal

    def add_obsticle(self, obsticle):
        self.obsticles += obsticle

    def intersects_obsticle_point(self, pos_x, pos_y):
        for obsticle in self.obsticles:
            if obsticle.contains(pos_x, pos_y):
                return True
        return False

    def intersects_obsticle(self, start_x, start_y, end_x, end_y):
        for obsticle in self.obsticles:
            if obsticle.intersects(start_x, start_y, end_x, end_y):
                return True
        return False
