from mathutils import distance
from environment import environment

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
        for (pos, node) in self.nodes:
            d = distance((pos_x, pos_y), pos)
            if d < min_distance:
                min_distance = d
                min_node = node
        return min_node
    
    def build_graph_from_environment(self, environment, width, height, res_x, res_y):
        x = 0
        x_step = width / res_x
        y_step = height / res_y
        delta = [(-x_step, 0), (-x_step, -y_step), (0, -y_step), (x_step, -y_step), (x_step, 0), (x_step, y_step), (0, y_step), (-x_step, y_step)]
        while x < width:
            y = 0
            while y < height:
                if not environment.intersects_obsticle_point(x, y):
                    self.add_node(graph_node(x, y))
                y += y_step
            x += x_step
        
        x = 0
        while x < width:
            y = 0
            while y < height:
                node = self.get_node(x, y)
                for (dx, dy) in delta:
                    adj_node = self.get_node(x + dx, y + dy)
                    if adj_node != None and not environment.intersects_obsticle(x, y, adj_node.get_pos_x(), adj_node.get_pos_y()):
                        node.add_adjacent(adj_node)
                y += y_step
            x += x_step
        
    def print_graph(self):
        for pos, node in self.nodes.items():
            print(str(pos))
            for adj in node.adjacent:
                print('  ' + str((adj.pos_x, adj.pos_y)))

class graph_node:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.adjacent = []
                
    def get_pos_x(self):
        return self.pos_x        
    
    def get_pos_y(self):
        return self.pos_y        
    
    def add_adjacent(self, adj_node):    
        self.adjacent.append(adj_node)                

g = graph()
g.build_graph_from_environment(environment(), 10, 10, 5, 5)
g.print_graph()