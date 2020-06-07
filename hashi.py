import os

map_max_x = 5
map_max_y = 5

map2 =[[2, 0, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [4, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [3, 0, 2, 0, 0]]


def print_map(aMap):
    for i in range(len(aMap)):
        if  i != 0:
                print ("")
        for j in range(len(aMap)):
            if j == len(aMap):
                print (str(aMap[i][j]), end = "")

            else:
                print (str(aMap[i][j]) + "" , end = "")

print_map(map2)

def find_islands(aMap):
    for i in range(len(aMap)):
        for j in range(len(aMap)):
            if aMap[i][j] != 0:
                return (i, j) # row, col