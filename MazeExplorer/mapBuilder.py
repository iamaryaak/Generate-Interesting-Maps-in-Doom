from omg import *
from mazeexplorer import *
import numpy as np
import cma
import random

# Global Variables
WALL = 1
EMPTY = 0

# print map 
def print_map(board):
	# Print the rows
	for r in board:
		#print(r)
		rowprint = ""
		for c in r:
			if c == WALL:
				rowprint = rowprint + "X"
			else:
				rowprint = rowprint + " "
		print(rowprint)


## TO DO
#  find representations for enemies and keys
##

# make sure to add floor/ceiling
def create_map():
	# create clear map any size (square map to begin with)
	# TODO: create any type of maps
	w = 10
	h = 10
	base_map = [[EMPTY for r in range(w)] for c in range(h)] 
	
	# TODO: add border around the map
	base_map = np.pad(base_map, pad_width=1, mode='constant', constant_values=WALL)
	print("==== Map with borders ====")
	print_map(base_map)

	nodes = []
	node_element = []
	# find appropriate wall points with direction (wall will be 2 spaces long)
	wall_points = []
	for i in range(20):
		x = random.randint(1, 9)
		y = random.randint(1, 9)
		wall_points.append((x,y))
		#print(wall_points)
		node_element = (x,y)
		nodes.append(wall_points)
		node_element = []

	for point in wall_points:
		#print(point)
		#print(base_map[point[0]][point[1]])
		base_map[point[0]][point[1]] = WALL
	
	# TODO: add a wall that goes up or right at these points
	# wall representations: [x, y, height, direction (right, down)]
	

	# print map
	print("==== Final Map ====")
	print_map(base_map)

	# save map as a .txt file
	with open('textMaps/testMap1.txt', 'w') as output_file:
		for row in base_map:
			rowprint = ""
			for c in row:
				if c == WALL:
					rowprint = rowprint + "X"
				else:
					rowprint = rowprint + " " 
			output_file.write(rowprint)
			output_file.write("\n")
	output_file.close()
	print(output_file, " is created!")
	return output_file

# main
maze_path = "tempfile"
maze_id = 3
# mazes = generate_mazes(maze_path, maze_id)

# create .txt representation of this
testMap1 = create_map()
