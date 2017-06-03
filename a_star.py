from mathutils import distance
from environment import environment
from graph import graph, graph_node
        
def heuristic(a, b):
    return distance([a.get_pos_x(), a.get_pos_y()], [b.get_pos_x(), b.get_pos_y()])

def build_a_star_graph(graph, environment, width, height, res_x, res_y):
    x = 0
    x_step = width / res_x
    y_step = height / res_y
    delta = [(-x_step, 0), (-x_step, -y_step), (0, -y_step), (x_step, -y_step), (x_step, 0), (x_step, y_step), (0, y_step), (-x_step, y_step)]
    while x < width:
        y = 0
        while y < height:
            if not environment.intersects_obsticle_point(x, y):
                g.add_node(graph_node(x, y))
            y += y_step
        x += x_step
    
    x = 0
    while x < width:
        y = 0
        while y < height:
            node = g.get_node(x, y)
            for (dx, dy) in delta:
                adj_node = g.get_node(x + dx, y + dy)
                if adj_node != None and not environment.intersects_obsticle(x, y, adj_node.get_pos_x(), adj_node.get_pos_y()):
                    node.add_adjacent(adj_node)
            y += y_step
        x += x_step
    
def find_a_star_path(graph, start_x, start_y, goal_x, goal_y):
    start = graph.get_closest(start_x, start_y)
    goal = graph.get_closest(goal_x, goal_y)
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
            return reconstruct_path(cameFrom, current)
        
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
    return total_path

g = graph()
build_a_star_graph(g, environment(None, None), 10, 10, 5, 5)
g.print_graph()

print(find_a_star_path(g, 0, 0, 8, 8))