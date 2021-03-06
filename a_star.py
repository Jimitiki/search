from mathutils import distance
from environment import environment
from graph import graph, graph_node
import plotutils
        
def heuristic(a, b):
    return distance([a.get_pos_x(), a.get_pos_y()], [b.get_pos_x(), b.get_pos_y()])

def build_a_star_graph(g, environment, res_x, res_y):
    x = 0
    x_step = environment.width / res_x
    y_step = environment.height / res_y
    delta = [(-x_step, 0), (-x_step, -y_step), (0, -y_step), (x_step, -y_step), (x_step, 0), (x_step, y_step), (0, y_step), (-x_step, y_step)]
    while x < environment.width:
        y = 0
        while y < environment.height:
            if not environment.intersects_obstacle_point(x, y):
                g.add_node(graph_node(x, y))
            y += y_step
        x += x_step
    
    x = 0
    while x < environment.width:
        y = 0
        while y < environment.height:
            node = g.get_node(x, y)
            if node != None:
                for (dx, dy) in delta:
                    adj_node = g.get_node(x + dx, y + dy)
                    if adj_node != None and not environment.intersects_obstacle(x, y, adj_node.get_pos_x(), adj_node.get_pos_y()):
                        node.add_adjacent(adj_node)
            y += y_step
        x += x_step
    
def find_a_star_path(environment, res_x, res_y):
    g = graph()
    build_a_star_graph(g, environment, res_x, res_y)
    (start_x, start_y) = environment.get_start()
    (goal_x, goal_y) = environment.get_goal()
    start = g.get_closest(start_x, start_y)
    goal = g.get_closest(goal_x, goal_y)
    closedSet = set()
    openSet = set([start])
    cameFrom = {}
    
    gScore = {}
    gScore[start] = 0
    fScore = {}
    fScore[start] = heuristic(start, goal)
    
    while len(openSet) > 0:
        current = min(openSet, key = lambda n: fScore[n])
        if current == goal:
            path = reconstruct_path(cameFrom, current)
            plotutils.plot_solution(path, g, environment)
            return path#reconstruct_path(cameFrom, current)
        
        openSet.remove(current)
        closedSet.add(current)
        for neighbor in current.adjacent:
            if neighbor in closedSet:
                continue
            tentative_gScore = gScore[current] + distance(current.get_position(), neighbor.get_position())
            if neighbor not in openSet:
                openSet.add(neighbor)
            elif tentative_gScore >= gScore[neighbor]:
                continue
            
            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic(neighbor, goal)
            
    return None
        
def reconstruct_path(cameFrom, current):
    total_path = [current.get_position()]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current.get_position())
    total_path.reverse()
    return total_path

#from graph import draw_path
#draw_path(find_a_star_path(environment((0, 0), (8, 8), 10, 10), 5, 5), 10, 10)
#
#g = graph()
#build_a_star_graph(g, environment(10, 10, 10, 10), 5, 5);
#g.show_graph(10, 10)
#g.print_graph()

#g = graph()
#n = graph_node(0, 0)
#n2 = graph_node(1, 1)
#n.add_adjacent(n2)
#g.add_node(n)
#g.add_node(n2)
#
#g.show_graph(2, 2)
#g.print_graph()
