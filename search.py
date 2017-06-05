from environment import environment, tag_obstacle
#import commands
import rrt
import a_star
import sys
import robot
import mathutils
from time import sleep


markers = {"96": {"corners": [[390.0, 321.0], [482.0, 319.0], [479.0, 395.0], [386.0, 398.0]], "center": [434.25, 358.25], "orientation": [0.04570382460951805, -0.9989550113677979]}, "97": {"corners": [[911.0, 315.0], [916.0, 386.0], [830.0, 386.0], [827.0, 314.0]], "center": [871.0, 350.25], "orientation": [0.9999826550483704, 0.00588225107640028]}, "98": {"corners": [[720.0, 387.0], [719.0, 313.0], [802.0, 312.0], [806.0, 385.0]], "center": [761.75, 349.25], "orientation": [-0.9998424649238586, 0.01774868369102478]}, "27": {"corners": [[268.0, 424.0], [360.0, 414.0], [359.0, 497.0], [267.0, 507.0]], "center": [313.5, 460.5], "orientation": [0.012047317810356617, -0.9999274015426636]}, "4": {"corners": [[1039.0, 312.0], [1117.0, 310.0], [1130.0, 380.0], [1050.0, 383.0]], "center": [1084.0, 346.25], "orientation": [-0.16779935359954834, -0.9858211874961853]}, "33": {"corners": [[365.0, 223.0], [277.0, 230.0], [279.0, 161.0], [366.0, 156.0]], "center": [321.75, 192.5], "orientation": [-0.022053459659218788, 0.9997568130493164]}, "30": {"corners": [[390.0, 152.0], [476.0, 147.0], [477.0, 214.0], [389.0, 219.0]], "center": [433.0, 183.0], "orientation": [0.0, -1.0]}, "94": {"corners": [[496.0, 394.0], [500.0, 319.0], [589.0, 317.0], [589.0, 391.0]], "center": [543.5, 355.25], "orientation": [-0.9996228814125061, 0.02746216580271721]}, "robot": {"corners": [[698.0, 763.0], [808.0, 766.0], [803.0, 878.0], [688.0, 875.0]], "center": [749.25, 820.5], "orientation": [0.06681464612483978, -0.9977654218673706]}, "26": {"corners": [[937.0, 311.0], [1016.0, 314.0], [1025.0, 385.0], [941.0, 383.0]], "center": [979.75, 348.25], "orientation": [-0.09053574502468109, -0.9958932399749756]}, "99": {"corners": [[816.0, 91.0], [894.0, 91.0], [899.0, 153.0], [821.0, 153.0]], "center": [857.5, 122.0], "orientation": [-0.08038418740034103, -0.9967639446258545]}, "21": {"corners": [[389.0, 303.0], [391.0, 236.0], [473.0, 229.0], [477.0, 296.0]], "center": [432.5, 266.0], "orientation": [-0.9966261386871338, 0.0820750892162323]}, "22": {"corners": [[845.0, 588.0], [840.0, 506.0], [923.0, 504.0], [928.0, 586.0]], "center": [884.0, 546.0], "orientation": [-0.9997097849845886, 0.02408939227461815]}, "23": {"corners": [[730.0, 600.0], [728.0, 516.0], [819.0, 513.0], [824.0, 595.0]], "center": [775.25, 556.0], "orientation": [-0.9990662932395935, 0.04320286586880684]}, "24": {"corners": [[1026.0, 507.0], [1035.0, 580.0], [946.0, 585.0], [939.0, 510.0]], "center": [986.5, 545.5], "orientation": [0.9989686012268066, -0.04540766403079033]}, "90": {"corners": [[241.0, 430.0], [241.0, 513.0], [140.0, 525.0], [143.0, 441.0]], "center": [191.25, 477.25], "orientation": [0.9933870434761047, -0.11481358110904694]}, "91": {"corners": [[974.0, 695.0], [965.0, 607.0], [1054.0, 603.0], [1066.0, 689.0]], "center": [1014.75, 648.5], "orientation": [-0.9984772801399231, 0.05516448989510536]}, "92": {"corners": [[918.0, 484.0], [830.0, 484.0], [827.0, 407.0], [912.0, 407.0]], "center": [871.75, 445.5], "orientation": [0.058342013508081436, 0.9982966780662537]}, "93": {"corners": [[481.0, 416.0], [476.0, 497.0], [382.0, 498.0], [386.0, 416.0]], "center": [431.25, 456.75], "orientation": [0.9999860525131226, -0.005290931556373835]}, "time": 785521.058103758, "95": {"corners": [[609.0, 397.0], [610.0, 322.0], [697.0, 320.0], [699.0, 394.0]], "center": [653.75, 358.25], "orientation": [-0.9996013045310974, 0.028237324208021164]}}


ADDRESS = ("0.0.0.0", 55555)

#commands.open_connection(ADDRESS)

#markers = commands.where_markers()

start_pos = markers["robot"]["center"]#commands.where_robot()["center"]
end_pos = markers[str(sys.argv[2])]["center"]
env = environment(start_pos, end_pos, 1000, 1600)

for marker_number in markers:
    if (marker_number == "time" or marker_number == str(sys.argv[2]) or marker_number == "robot"):
        continue
    env.add_obstacle(tag_obstacle(markers[marker_number]))

if sys.argv[1] == "-astar":
    path = a_star.find_a_star_path(env, 20, 20)
elif sys.argv[1] == "-rrt":
    path = rrt.solve(env, 100)
else:
    exit()

exit()
"""
for position in path:
    print(position)
    sleep(3)
    at_position = False
    while not at_position:
        robot_position = commands.where_robot()["center"]
        vector = (position[0] - robot_position[0], position[1] - robot_position[1])
        vector = mathutils.normalize(vector[0], vector[1])
        at_position = robot.follow_vector(vector[0] * 8, vector[1] * 8, position)

commands.close_connection()"""
