import matplotlib.pyplot as plt

def plot_solution(path, graph, env):
    (width, height) = env.get_dimensions()
    plt.ylim([0, height])
    plt.xlim([0, width])
    draw_graph(graph, height)
    draw_environment(env, height)
    draw_path(path, height)
    plt.show()

def draw_graph(graph, height):
    for pos, node in graph.get_nodes().items():
        #reflect in the y direction
        offset_pos_y = height - pos[1]
        for adj in node.adjacent:
            dx = adj.get_pos_x() - pos[0]
            plt.arrow(pos[0], offset_pos_y, dx, -adj.get_pos_y() + pos[1])

def draw_environment(env, height):
    for obstacle in env.get_obstacles():
        (p1, p2, p3, p4) = obstacle.get_rect()
        draw_square_from_vertices(p1, p2, p3, p4, "m", height)

    draw_square_from_center(env.get_start(), 50, "y", height)
    draw_square_from_center(env.get_goal(), 50, "r", height)

def draw_square_from_center(center, size, color, height):
    p1 = (center[0] - size, center[1] - size)
    p2 = (center[0] + size, center[1] - size)
    p3 = (center[0] + size, center[1] + size)
    p4 = (center[0] - size, center[1] + size)
    draw_square_from_vertices(p1, p2, p3, p4, color, height)

def draw_square_from_vertices(p1, p2, p3, p4, color, height):
    plt.arrow(p1[0], height - p1[1], p2[0] - p1[0], -p2[1] + p1[1], ec=color)
    plt.arrow(p2[0], height - p2[1], p3[0] - p2[0], -p3[1] + p2[1], ec=color)
    plt.arrow(p3[0], height - p3[1], p4[0] - p3[0], -p4[1] + p3[1], ec=color)
    plt.arrow(p4[0], height - p4[1], p1[0] - p4[0], -p1[1] + p4[1], ec=color)

def draw_path(path, height):
    for i in range(0, len(path) - 1):
        plt.arrow(path[i][0], height - path[i][1], path[i + 1][0] - path[i][0], -path[i + 1][1] + path[i][1], ec="g")
