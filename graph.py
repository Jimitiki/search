from mathutils import distance
from environment import environment
import matplotlib.pyplot as plt

class graph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[(node.get_pos_x(), node.get_pos_y())] = node

    def get_node(self, pos_x, pos_y):
        try:
            return self.nodes[(pos_x, pos_y)]
        except:
            return None

    def get_closest(self, pos_x, pos_y):
        min_node = None
        min_distance = float('inf')
        for pos, node in self.nodes.items():
            d = distance((pos_x, pos_y), pos)
            if d < min_distance:
                min_distance = d
                min_node = node
        return min_node

    def print_graph(self):
        for pos, node in self.nodes.items():
            print(str(pos))
            for adj in node.adjacent:
                print('  ' + str((adj.pos_x, adj.pos_y)))
    
    def show_graph(self, width, height):
        plt.ylim([0, height])
        plt.xlim([0, width])
        for pos, node in self.nodes.items():
            for adj in node.adjacent:
                plt.arrow(pos[0], pos[1], adj.get_pos_x() - pos[0], adj.get_pos_y() - pos[1], head_width = width / 40.0, head_length = width / 40.0)
        plt.show()
        
class graph_node:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.adjacent = []

    def __eq__(self, other):
        return self.pos_x == other.pos_x and self.pos_y == other.pos_y
    
    def __hash__(self):
        return hash((self.pos_x, self.pos_y))
                
    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def get_position(self):
        return (self.pos_x, self.pos_y)

    def add_adjacent(self, adj_node):
        self.adjacent.append(adj_node)

def draw_path(path, width, height):
    plt.ylim([0, height])
    plt.xlim([0, width])
    for i in range(0, len(path) - 1):
        plt.arrow(path[i][0], path[i][1], path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1], head_width = width / 40.0, head_length = width / 40.0)
    plt.show()
