from environment import environment, tag_obstacle
import commands
import rrt
import a_star
import sys

def get_obstacle_from_marker(marker):


ADDRESS = ("0.0.0.0", 55555)

commands.open_connection(ADDRESS)

markers = commands.where_markers()

start_pos = commands.where_robot()["center"]
end_pos = markers[str(sys.argv[2])]["center"]
env = environment(start_pos, end_pos)

for marker_number in markers:
    env.add_obstacle(get_obstacle_from_marker(markers[marker_number]))

search_method = rrt.rrt() if sys.argv[1] == "rrt" else a_star.a_star()

commands.close_connection()
