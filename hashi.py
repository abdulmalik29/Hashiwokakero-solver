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

# a fuction that locate all island in the map ,
# returns their x and coord and their number
# store them form LEFT to RIGHT , from TOP tom BOTTOM

def locate_islands(aMap): 
    islands = []
    for x in range(len(aMap)):
        for y in range(len(aMap)):
            if aMap[x][y] != 0:
                # print("x = ", str(x), ", y = ", str(y)) #debugging tool
                # x = island x , y = islands y , aMap[x][y]] = the island number
                islands.append([x, y, aMap[x][y]])
    # print(islands) #debugging tool
    return islands


def find_nearby_islands(aMap, num, island):
    
    for i in range(len(aMap[0])): #check horazontly
        if aMap[island[0]][i] == num and island[1] != i:
            return False
    
    for j in range(len(aMap)): #check vetackly
        if aMap[j][island[1]] == num and island[0] != j:
            return False

islands = locate_islands(map2)

#print_map(map2)
# print(islands)
# print(islands[4][0])
# locate_islands(map2)
# find_nearby_islands(map2)

print("________________________________")

for number_of_island in range(len(islands)):  # check horazontly by island x coords
    for i in map2[islands[number_of_island][0]]:
            print(i)


# print("===================")
# counter = 0
# for j in range(len(map2)):  # check vertically
#     if counter < 3:
#         print(map2[j][3])
#         counter +=  1
