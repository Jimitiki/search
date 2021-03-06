from environment import environment, tag_obstacle
import commands
import rrt
import a_star
import sys
import robot
import mathutils
from time import sleep
import json

#json_data = open(".\config.json").read()
#markers = json.loads(json_data)

ADDRESS = ("0.0.0.0", 55555)

commands.open_connection(ADDRESS)

markers = commands.where_markers()

#start_pos = markers["robot"]["center"]
start_pos = commands.where_robot()["center"]
end_pos = markers[str(sys.argv[2])]["center"]
env = environment(start_pos, end_pos, 1000, 1600)

for marker_number in markers:
    if (marker_number == "time" or marker_number == str(sys.argv[2]) or marker_number == "robot"):
        continue
    env.add_obstacle(tag_obstacle(markers[marker_number]))

if sys.argv[1] == "-astar":
    path = a_star.find_a_star_path(env, 16, 16)
elif sys.argv[1] == "-rrt":
    path = rrt.solve(env, 90)
else:
    exit()

for position in path:
    at_position = False
    while not at_position:
        robot_position = commands.where_robot()["center"]
        vector = (position[0] - robot_position[0], position[1] - robot_position[1])
        vector = mathutils.normalize(vector[0], vector[1])
        at_position = robot.follow_vector(vector[0] * 6, vector[1] * 6, position)

commands.set_speed(0, 0)

commands.close_connection()
