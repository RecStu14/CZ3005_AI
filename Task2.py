import json, timeit
from collections import deque # deque = Doubly Ended Queue

def sortEcost(node, nlist, Cost):
    Q = deque()
    Q.append(nlist[0])
    ptr = 0

    for adj in nlist[1:]:
        while ptr < len(Q):
            if Cost[node+","+adj] <= Cost[node+","+nlist[ptr]]:
                Q.appendleft(adj)
                break
            elif ptr == len(Q)-1:
                Q.append(adj)
            else:
                ptr+=1
    return Q

# g - python dict, v - start node, w - end node
def UCS(g, Dist, Cost, v, w):
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
        list = sortEcost(ptr, g[ptr], Cost)
        for adj in list:
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

            

        # if no more nodes connected to source vertex
        if len(Pqueue) == 0:
            break        
        ptr = Pqueue.popleft()
    print()
    # A path to target vertex is found that fulfills all condition
    return d[int(w)-1]
   
        
def run_task2():
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
        start = input("Please enter the start node: ")
        end = input("Please enter the end node: ")
        
        t2 = timeit.default_timer()
        path = UCS(G_dict, Dist, Cost, start, end)
        t3 = timeit.default_timer()

        if path[0] is not None:
            #print("Path Length: " + str(len(path[2])))
            print("Shortest Path:\n",)
            #for node in path[2]:
                #print(node, end ="->")
            print(" -> ".join(path[2]))
            print("Shortest Distance: " + str(path[0]))
            print("Total Energy Cost: " + str(path[1]))
            print("\n")
            #print("Time taken: " + str(round(t3-t2, 3)))
        else:
            print("Cannot find path within budget")
            print("Time taken: " + str(round(t3-t2, 3)))
            
        again = input("Do you want to find path again? [y/n]")

    # Closing file
    f.close()