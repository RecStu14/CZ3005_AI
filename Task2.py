import json, timeit
from collections import deque # deque = Doubly Ended Queue

def DFS(g, Dist, Cost, v, w):
    # Queue to record adjacent nodes
    Pqueue = deque()
    count = 0

    # initialize list of (route, distCost, eCost) tuples from source vertex
    d = []
    d = [ [ [], None, None] for i in range(len(g))] # infinity dist from source vertex = no path to target vertex

    d[int(v)-1][0].append(v)
    d[int(v)-1][1] = 0
    d[int(v)-1][2] = 0
    ptr = v

    t1 = timeit.default_timer()
    
    # while target vortex is not reached
    while not d[int(w)-1][0]:
        for adj in g[ptr]:
            tmp = d[int(ptr)-1][0][:]
    
            # only expand if unvisited
            if tmp.count(adj) < 1:
                Pqueue.appendleft(adj)
                dCost = d[int(ptr)-1][1] + Dist[ptr+","+adj]
                eCost = d[int(ptr)-1][2] + Cost[ptr+","+adj]
                
                if eCost <= 287932: 
                    tmp.append(adj)
                    
                    # if not visited before, add prev distCost and edgeCost
                    if d[int(adj)-1][1] is None:
                        d[int(adj)-1][0] = tmp[:]
                        d[int(adj)-1][1] = dCost
                        d[int(adj)-1][2] = eCost
                        
                    # if visited but a better path found, replace
                    elif dCost < d[int(adj)-1][1] and eCost < d[int(adj)-1][2]:
                        d[int(adj)-1][0] = tmp[:]
                        d[int(adj)-1][1] = dCost
                        d[int(adj)-1][2] = eCost
                        
            
        t2 = timeit.default_timer()

        #if no more nodes to expand or (t2-t1) > 15, break and return
        if len(Pqueue) == 0 or (t2-t1) >= 15:
            break
        ptr = Pqueue.popleft()
        
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
    path = DFS(G_dict, Dist, Cost, start, end)
    t3 = timeit.default_timer()

    if not path[0]: #if empty list returned
        print("No path connecting " + start + " to " + end)
    else:
        print("Shortest Path:", end = " ")
        for node in path[0]:
            print(node, end ="->")
        print()
        print("Shortest Distance: " + str(path[1]))
        print("Total Energy Cost: " + str(path[2]))
        print("Time taken: " + str(round(t3-t2, 3)))
        
    again = input("Do you want to find path again? (y/n)")
# Closing file
f.close()
