import random
import mathutils
from graph import graph, graph_node

class rrt(graph):

    def __init__(self):
        graph.__init__(self)

    def build_graph_from_environment(self, env, width, height, edge_length):
        root = graph_node(env.get_start()[0], env.get_start()[1])
        self.add_node(root)
        goal = env.get_goal()
        end_node = None
        is_complete = False
        while not is_complete:
            point = self.generate_point(env)
            neighbor = self.get_closest(point[0], point[1])
            new_node = self.get_new_node(neighbor, point, env, edge_length)
            if self.is_valid_edge(new_node, neighbor):
                new_node.add_adjacent(neighbor)
                self.add_node(new_node)
                if mathutils.distance(new_node.get_position, goal):
                    is_complete = True
                    end_node = graph_node(goal[0], goal[1])
                    end_node.add_adjacent(new_node)
        self.build_path(end_node)
        return self.path

    def generate_point(self, env):
        return (0, 0)

    def get_new_node(self, init_node, point, env, edge_length):
        node_pos = init_node.get_position()
        if mathutils.distance(node_pos, point) > edge_length:
            #normalize vector difference
            diff_vector = mathutils.normalize(node_pos[0] - point[0], node_pos[1] - point[1])
            #multiply normalized vector by the max distance
            diff_vector[0] *= edge_length
            diff_vector[1] *= edge_length
            #add to original node
            new_position = (node_pos[0] + diff_vector[0], node_pos[1] + diff_vector[1])
            return graph_node(new_position[0], new_position[1])

        return graph_node(point[0], point[1])

    def is_valid_edge(self, node1, node2):
        return True

    def build_path(self, end_node):
        cur_node = end_node
        while len(cur_node.adjacent) > 0:
            self.path.insert(0, cur_node)
            cur_node = cur_node.adjacent[0]