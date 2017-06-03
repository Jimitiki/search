import random
import mathutils
from graph import graph, graph_node
import random

def solve(env, edge_length):
    tree = graph()
    root = graph_node(env.get_start()[0], env.get_start()[1])
    tree.add_node(root)
    goal = env.get_goal()
    (width, height) = env.get_dimensions()
    end_node = None
    is_complete = False
    while not is_complete:
        point = generate_point(width, height)
        neighbor = tree.get_closest(point[0], point[1])
        new_node = get_new_node(neighbor, point, env, edge_length)
        if is_valid_edge(new_node, neighbor):
            new_node.add_adjacent(neighbor)
            tree.add_node(new_node)
            if mathutils.distance(new_node.get_position, goal) <= edge_length:
                is_complete = True
                end_node = graph_node(goal[0], goal[1])
                end_node.add_adjacent(new_node)
    build_path(end_node)
    return self.path

def generate_point(self, width, height):
    x = random.random() * width
    y = random.random() * height
    return (x, y)

def get_new_node(self, init_node, point, edge_length):
    node_pos = init_node.get_position()
    if mathutils.distance(node_pos, point) >= edge_length:
        #normalize vector difference
        diff_vector = mathutils.normalize(node_pos[0] - point[0], node_pos[1] - point[1])
        #multiply normalized vector by the max distance
        diff_vector[0] *= edge_length
        diff_vector[1] *= edge_length
        #add to original node
        new_position = (node_pos[0] + diff_vector[0], node_pos[1] + diff_vector[1])
        return graph_node(new_position[0], new_position[1])

    return graph_node(point[0], point[1])

def is_valid_edge(self, env, node1, node2):
    (x1, y1) = node1.get_position
    (x2, y2) = node2.get_position
    return env.intersects_obstacle(x1, x2, y1, y2)

def build_path(self, end_node):
    path = []
    cur_node = end_node
    while len(cur_node.adjacent) > 0:
        path.insert(0, cur_node.get_position())
        cur_node = cur_node.adjacent[0]
    return path
