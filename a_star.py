from mathutils import distance
from environment import environment
from graph import graph, graph_node

class a_star(graph):
    def __init__(self):
        graph.__init__(self)
    
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

g = a_star()
g.build_graph_from_environment(environment((0, 0),(10, 10)), 10, 10, 5, 5)
g.print_graph()