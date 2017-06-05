import random
import mathutils
from graph import graph, graph_node
import plotutils

def solve(env, edge_length):
    tree = graph()
    root = graph_node(env.get_start()[0], env.get_start()[1])
    tree.add_node(root)
    goal = env.get_goal()
    (width, height) = env.get_dimensions()
    end_node = None
    is_complete = False
    while not is_complete:
        point = generate_point(width, height, 100)
        neighbor = tree.get_closest(point[0], point[1])
        new_node = get_new_node(neighbor, point, edge_length)
        if is_valid_edge(env, new_node, neighbor):
            new_node.add_adjacent(neighbor)
            tree.add_node(new_node)
            if mathutils.distance(new_node.get_position(), goal) <= edge_length:
                is_complete = True
                end_node = graph_node(goal[0], goal[1])
                end_node.add_adjacent(new_node)
    path = build_path(end_node)
    build_path(end_node)
    plotutils.plot_solution(path, tree, env)
    return path#build_path(end_node)

def generate_point(width, height, margin):
    x = random.random() * (width - 2 * margin)
    y = random.random() * (height - 2 * margin)
    return (x + margin, y + margin)

def get_new_node(init_node, point, edge_length):
    node_pos = init_node.get_position()
    if mathutils.distance(node_pos, point) >= edge_length:
        new_position = mathutils.move_point_towards_point(node_pos, point, edge_length)
        return graph_node(new_position[0], new_position[1])

    return graph_node(point[0], point[1])

def is_valid_edge(env, node1, node2):
    (x1, y1) = node1.get_position()
    (x2, y2) = node2.get_position()
    return not env.intersects_obstacle_point(x1, y1) and not env.intersects_obstacle(x1, y1, x2, y2)

def build_path(end_node):
    path = []
    cur_node = end_node
    while len(cur_node.adjacent) > 0:
        path.insert(0, cur_node.get_position())
        cur_node = cur_node.adjacent[0]
    return path
