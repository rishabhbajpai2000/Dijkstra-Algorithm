
import sys
# inputting the data.
inf = sys.maxsize
graph = [[0, 6, inf, 1, inf],
         [6, 0, 5, 2, 2],
         [inf, 5, 0, inf, 5],
         [1, 2, inf, 0, 1],
         [inf, 2, 5, 1, 0]]
graph_2 = [[0, 27,	inf,	inf,	inf,	inf,	inf,	inf,	inf,	inf],
           [27,	0,	3,	inf,	inf,	inf,	1,	7,	inf,	inf],
           [inf,	3,	0,	2,	22,	inf,	inf,	9,	inf,	inf],
           [inf,	inf,	2,	0,	17,	inf,	inf,	inf,	inf,	inf],
           [inf,	inf,	22,	17,	0,	15,	inf,	inf,	inf,	inf],
           [inf,	inf,	inf,	inf,	15,	0,	inf,	11,	inf,	inf],
           [inf,	1,	inf,	inf,	inf,	inf,	0,	inf,	inf,	inf],
           [inf,	7,	9,	inf,	inf,	11,	inf,	0,	inf,	5],
           [inf,	inf,	inf,	inf,	inf,	inf,	inf,	inf,	0,	1],
           [inf,	inf,	inf,	inf,	inf,	inf,	inf,	11,	1,	0]]

def dijkstra_list(graph, s_v):
    # graph list[ith vertex] = [shortest path, previous vertex, visited]
    list = []
    for i in range(len(graph)):
        if i == s_v:
            list.append([0,-1, False])
        else:
            list.append([sys.maxsize, -1, False])
    # debug: print(list)
    
    while True:
    #finding the element with lowest distance and that is not already visited
        minm = sys.maxsize
        ind = 0
        for i in range(len(list)):
            if list[i][0] < minm and list[i][2] == False:
                minm = list[i][0]
                ind = i
        #debug: print("minimum size element is " + str(ind)) 
        # finding the neighbors of the smallest element in the graph
        neighbor = []
        for i in range(len(graph[ind])):
            if graph[ind][i] not in [0, inf]:
                neighbor.append(i)
        #debug: print(f'the nighbours of {ind} are {neighbor}')

        # now balancing the weight of the neighbours
        for i in neighbor:
            curr_wei_i = list[i][0] 
            curr_wei_ind = list[ind][0]
            new_wei = curr_wei_ind + graph[ind][i]
            #debug: print(" ")
            #debug: print("i = " + str(i))
            #debug: print("curr_wei_i = " + str(curr_wei_i))
            #debug: print("new_wei = " + str(new_wei))
            #debug: print(" ")
            if new_wei < curr_wei_i:
                list[i][0] = new_wei
                list[i][1] = ind
                #debug: print(list)
        # adding the lowest weight index of the list to visited ones and removing it from list
        list[ind][2] = True 
        #debug:print(list)
        #debug: print("-----------------------------------------")

        # stopping the loop when all visited. 
        # counting the number of trues in the list, and if that is equal to the number of items in the list then stop
        true_num = 0
        for i in list:
            if i[2] == True:
                true_num += 1
        if true_num == len(list):
            return list

def dijkstra(graph, s_v, e_v):
    list = dijkstra_list(graph, s_v)
    #debug: print(list)
    dest = e_v
    ans = [e_v]
    while True:
        #debug: print(ans)
        dest = list[dest][1]
        if dest == -1:
            break
        ans.append(dest)

    print(ans[::-1])

dijkstra(graph_2,1,5)