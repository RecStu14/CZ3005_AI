import json, timeit
from collections import deque # deque = Doubly Ended Queue

# g - python dict, v - start node, w - end node
def BFS(g, Dist, Cost, v, w):
    # Queue to record adjacent nodes
    Pqueue = deque()
    
    seen = []
    # initialize list of (distCost, eCost, route) tuples from source vertex
    d = []
    d = [ [None, None, []] for i in range(len(g))] # infinity dist from source vertex = no path to target vertex

    d[int(v)-1][0] = 0 #indicate source vertex
    d[int(v)-1][1] = 0 #indicate source vertex
    d[int(v)-1][2].append(v)
    seen.append(v)
    ptr = v

    # while target vortex is not reached
    while True:
        for adj in g[ptr]:
            eCost = d[int(ptr)-1][1] + Cost[ptr+","+adj]
            
            # if unvisited and within budget
            if seen.count(adj) < 1:
                if eCost <= 287932:
                    seen.append(adj) # mark visited
                    Pqueue.append(adj)

                    dCost = d[int(ptr)-1][0] + Dist[ptr+","+adj]
                    tmp = d[int(ptr)-1][2][:]
                    tmp.append(adj) 

                    d[int(adj)-1][0] = dCost
                    d[int(adj)-1][1] = eCost
                    d[int(adj)-1][2] = tmp[:]

            # if visited but a better path found, replace
            elif eCost < d[int(adj)-1][1]:
                Pqueue.appendleft(adj)

                dCost = d[int(ptr)-1][0] + Dist[ptr+","+adj]
                tmp = d[int(ptr)-1][2][:]
                tmp.append(adj)

                d[int(adj)-1][0] = dCost
                d[int(adj)-1][1] = eCost
                d[int(adj)-1][2] = tmp[:]

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
    
    t2 = timeit.default_timer()
    path = BFS(G_dict, Dist, Cost, start, end)
    t3 = timeit.default_timer()

    if path[0] is not None:
        print("Path Length: " + str(len(path[2])))
        print("Shortest Path:", end = " ")
        for node in path[2]:
            print(node, end ="->")
        print()
        print("Shortest Distance: " + str(path[0]))
        print("Total Energy Cost: " + str(path[1]))
        print("Time taken: " + str(round(t3-t2, 3)))
        
    again = input("Do you want to find path again? (y/n)")

# Closing file
f.close()
