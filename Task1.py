#TASK 1 - Dijkstra Algorithm

#Importing the Libraries
from heapq import heappush, heappop
import creating_new_format_task1 as CNF
import sys 

def run_task1():
    print("Running Task 1: Dijkstra Algorithm ... ")

    #importing the graph <dictionary> from creating_new_format.py
    graph = CNF.graph

    #getting user input for the start and goal node
    start_node = input("Please enter the start node: ")
    goal_node = input("Please enter the goal node: ")

    #creating an infinte value - sys.maxsize returns the max value it can hold
    INFINITE = sys.maxsize 

    #Getting the number of nodes and edges
    num_nodes = CNF.num_nodes
    num_edges = CNF.num_edges

    def dijkstra(graph, start_node, goal_node):
        #getting the keys of the neighbours dictionary
        neighbours_keys = CNF.get_keys('neighbours')

        #initialising empty dictionaries to track the various factors
        distances = {} #tracks the distance
        predecessors = {} #tracks the path
        
        #assigning the initial values to the nodes
        for node in neighbours_keys:
            distances[node] = INFINITE
            predecessors[node] = ""

        #assigning the distance of only the start node as 0 to begin 
        distances[start_node] = 0

        #list of a tuple - first entry to the minheap where the first element 0 - distance, second element
        #start_node - the name of the node
        min_heap = [(0,start_node)] 

        #to keep track of the nodes visited - using set() as it only accepts unique nodes, so we don't 
        #visit a node more than once
        visited = set() 
        
        #while the min_heap is not empty
        while min_heap:
            #pops and returns the smallest distance and its corresponding node in the heap
            current_dist, current_node = heappop(min_heap)

            #break the loop is the current_node is the goal_node
            if current_node == goal_node:
                break

            #if the current_node has already been visited control is returned to the begining of the while
            #loop in line 53
            if current_node in visited: 
                continue

            #add the current_node to the visited set
            visited.add(current_node)    
            
            #iterating through all the neighbours of the current_node 
            for neighbour,dist in graph[current_node]:

                #if the neighbour has been visited return control to the for loop in line 70
                if neighbour in visited: 
                    continue

                #calculate the distance taken - which is the sum of the distance of the current_node and the
                #distance taken to reach the neighbour
                this_dist = current_dist + dist
                
                #replace the existing distance value with the new calculated distance (this_dist) only if
                #the calculated distance is lesser than the existing distance
                if this_dist  < distances[neighbour]:

                    #replacing the existing distance with the calculated distance
                    distances[neighbour] = this_dist

                    #pushing the a new tuple with the neighbour node and its new calculated distance into
                    #the minheap min_heap
                    heappush(min_heap, (this_dist, neighbour))

                    #updating the predecessors dictionary
                    predecessors[neighbour] = current_node
                    
                    
        #Displaying the Output

        #calling the get_path() function and formatting the path to include '->' and displaying it
        path = get_path(predecessors, goal_node)
        str_path = " -> ".join(path)
        print("Shortest Path:\n", str_path)

        #displaying the shortest distance taken
        print('Shortest Distance:', distances[goal_node])

        #displaying the total energy cost by calling the get_energy_cost() function
        print('Total Energy Cost:', get_energy_cost(predecessors, goal_node))

        print("\n")
        

    #Function to get the path from the start_node to the goal_node from the predecessors dictionary
    def get_path(predecessors, goal_node):
        #need to append all the predecessors into a new list to display it in the format required by the 
        #question
        path = []

        while goal_node != "":
            path.append(goal_node)
            goal_node = predecessors[goal_node]
        #need to reverse the path in order to get the path from start_node to the goal_node
        path.reverse()

        return path

    #Function to get the total energy cost
    def get_energy_cost(predecessors, goal_node):
        #calling the get_path() function to know the nodes that have been visited
        path = get_path(predecessors, goal_node)

        #assign an inital cost of 0 to the energy cost
        energy_cost = 0

        #for the predecessors that have been visited sum up the respective energy costs
        for i in range(1, len(path)):
            energy_cost += CNF.get_cost(path[i-1], path[i])

        return energy_cost


    #create a dictionary the contains a list to keep track of cost and predecessors    
    def create_cost_pred_dict():
        #getting the keys of the neighbours dictionary
        neighbours_keys = CNF.get_keys('neighbours')

        #initialising empty dictionary and list
        final_cost_pred_dict = {}
        min_heap = []

        #initialising every node in the neighbours keys
        for node in neighbours_keys:
            cost_pred_dict = {}
            cost_pred_dict['Predecessor'] = ""
            final_cost_pred_dict[node] = cost_pred_dict

            #pushing the tuple into the minheap min_heap
            heappush(min_heap, (cost_pred_dict['Cost'], node))

        return final_cost_pred_dict, min_heap

    #calling the dijkstra function()
    dijkstra(graph, start_node, goal_node)  
  


