import json, timeit
from collections import deque # deque = Doubly Ended Queue

# g - python dict, v - start node, w - end node
def BFS(g, Dist, Cost, v, w):
    # Priority Queue
    Pqueue = deque()
    

    # initialize list of (distCost, eCost, route) tuples from source vertex
    d = []
    d = [ [None, None, []] for i in range(len(g))] # infinity dist from source vertex = no path to target vertex

    d[int(v)-1][0] = 0 #indicate source vertex
    d[int(v)-1][1] = 0 #indicate source vertex
    d[int(v)-1][2].append(v)

    ptr = v

    # while target vortex is not reached
    while d[int(w)-1][0] is None:
        for adj in g[ptr]:
            tmp = d[int(ptr)-1][2][:]
            if tmp.count(adj) < 1:
                Pqueue.append(adj)
                dCost = d[int(ptr)-1][0] + Dist[ptr+","+adj]
                eCost = d[int(ptr)-1][1] + Cost[ptr+","+adj]
                # if within eCost budget, continue expanding nodes
                if eCost <= 287932:
                    tmp.append(adj)
                    # if not visited before, add prev distCost and edgeCost
                    if d[int(adj)-1][0] is None:
                        d[int(adj)-1][0] = dCost
                        d[int(adj)-1][1] = eCost
                        d[int(adj)-1][2] = tmp[:]
                    elif dCost < d[int(adj)-1][0] and eCost < d[int(adj)-1][1]:
                        d[int(adj)-1][0] = dCost
                        d[int(adj)-1][1] = eCost
                        d[int(adj)-1][2] = tmp[:]
                else:
                    print(tmp + "cannot expand further due to budget")
        # if no more nodes connected to source vertex
        if len(Pqueue) == 0:
            break        
        ptr = Pqueue.popleft()
    print()
    # A path to target vertex is found that fulfills all condition
    return d[int(w)-1]
   
        
# Open JSON file
f = open('G.json')
f1 = open('Dist.json')
f2 = open('Cost.json')

# convert to Python dictionary (node n, list of adjacent nodes)
G_dict = json.load(f)
Dist = json.load(f1)
Cost = json.load(f2)
again = "y"
while again == "y":
    start = input("start node [1-264346]: ")
    end = input("end node [1-264346]: ")
    
    t1 = timeit.default_timer()
    path = BFS(G_dict, Dist, Cost, start, end)
    t2 = timeit.default_timer()

    if all(ele is None for ele in path):
        print("No path connecting " + start + " to " + end)
    else:
        print("Shortest Path:", end = " ")
        for node in path[2]:
            print(node, end ="->")
        print()
        print("Shortest Distance: " + str(path[0]))
        print("Total Energy Cost: " + str(path[1]))
        print("Time taken: " + str(round(t2-t1, 3)))
        
    again = input("Do you want to find path again? (y/n)")

# Closing file
f.close()
