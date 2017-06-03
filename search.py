from environment import environment, tag_obstacle
import commands
import rrt
import a_star
import sys
import robot
import mathutils
from time import sleep

ADDRESS = ("0.0.0.0", 55555)

commands.open_connection(ADDRESS)

markers = commands.where_markers()

start_pos = commands.where_robot()["center"]
end_pos = markers[str(sys.argv[2])]["center"]
env = environment(start_pos, end_pos, 1600, 1000)

for marker_number in markers:
    if (marker_number == "time"):
        continue
    env.add_obstacle(tag_obstacle(markers[marker_number]["corners"]))

if sys.argv[1] == "-astar":
    path = a_star.find_a_star_path(env, 1600, 1000, 200, 200)
elif sys.argv[1] == "-rrt":
    path = rrt.solve(env, 300)
else:
    exit()

for position in path:
    print(position)
    sleep(3)
    at_position = False
    while not at_position:
        robot_position = commands.where_robot()["center"]
        vector = (position[0] - robot_position[0], position[1] - robot_position[1])
        vector = mathutils.normalize(vector[0], vector[1])
        at_position = robot.follow_vector(vector[0] * 8, vector[1] * 8, position)

commands.close_connection()
