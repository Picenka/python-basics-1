import itertools
point_1 = (0, 2)  # координаты  точки
point_2 = (2, 5)  # координаты  точки
point_3 = (5, 2) # координаты  точки
point_4 = (6, 6)  # координаты  точки
point_5 = (8, 3)  # координаты  точки
list_point=[point_1,point_2,point_3,point_4,point_5]
ways=[]
path_tree=[]
def leng (list_point):
    summ=0.0
    output_string=''
    for i in range(len(list_point)):
        if list_point[0]==list_point[i+1]:
            summ+=((list_point[i+1][0] - list_point[i][0]) ** 2 + (list_point[i+1][1] - list_point[i][1]) ** 2) ** 0.5
            output_string += (f'{list_point[i]} -> {list_point[i + 1]} = {summ} ')
            break
        else:
            summ+=((list_point[i+1][0] - list_point[i][0]) ** 2 + (list_point[i+1][1] - list_point[i][1]) ** 2) ** 0.5
            output_string += (f'{list_point[i]} -> {list_point[i + 1]}{summ} ')
    return summ,output_string

for tree in itertools.permutations(list_point):
    list_tree = list(tree)
    list_tree.append(list_point[0])
    if list_point[0]==list_tree[0]:
        path_tree.append(list_tree)
    else:
         break

for i in path_tree:
    ways.append(leng(i))
for i in path_tree:
    if min(ways)==leng(i):
        print(min(ways)[1])
        break