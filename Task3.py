#TASK 3 - A*STAR Algorithm
import math


class Graph:
    def __init__(self, adjac_lis, coord_lis):
        self.adjac_lis = adjac_lis
        self.coord_lis = coord_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    def get_coord(self, v):
        return self.coord_lis[v]

    def heuristics(self, v, stop):
        #return self.calculate_manhattan(self.get_coord(stop),self.get_coord(v))
        #return self.calculate_edist(self.get_coord(stop),self.get_coord(v))
        return self.calculate_diagonal(self.get_coord(stop),self.get_coord(v))

    #def calculate_manhattan(self,e_coord, v_coord):
    #    return cityblock(v_coord,e_coord)

    def calculate_edist(self, e_coord, v_coord):
        x1, y1 = e_coord[0], e_coord[1]
        x2, y2 = v_coord[0], v_coord[1]
        result = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
        return result

    def calculate_diagonal(self, e_coord, v_coord):
        x1, y1 = e_coord[0], e_coord[1]
        x2, y2 = v_coord[0], v_coord[1]
        x = abs(x2 - x1)
        y = abs(y2 - y1)
        d = 1
        result = d * (x + y) + (math.sqrt(2) - 2*d) * min(x,y)
        return result

    def return_path(self, parent, n):
        path = []
        # Add in the ending node
        path.append(n)

        while parent[n] != n:
            n = parent[n]
            path.append(n)

        path.reverse()

        return path

    def print_result(self, path):
        print("Shortest Path:\n" + " -> ".join(path))

    def a_star(self, start, stop, max_energy):

        # A star = g(n) + h(n)
        # g(n) is the actual distance cost from start -> current node
        # h(n) is the estimated cost from current node -> end node

        # Open List : Nodes that are pending to be examined
        open_list = set([start])
        # Closed List : Nodes that are examined
        closed_list = set([])

        # g(n) has the shortest accumulated distances from start to particular node
        g = {}
        g[start] = 0

        # energy_cost is the accumulated energy cost from start to particular node
        energy_cost = {}
        energy_cost[start] = 0

        # parent contains the linkage to from the parent to the child node
        parent = {}
        parent[start] = start

        # Initialise the start node
        current = start

        while open_list:

            #Finding the node with the lowest f(n) value - In the open list
            for node in open_list:

                # Let the currentNode/ Active Node be equals to the node with the least f value.
                if g[node] + self.heuristics(node, stop) < g[current] + self.heuristics(current, stop):
                    current = node

            # Solution is found!
            if current == stop:
                path = self.return_path(parent, stop)
                self.print_result(path)
                print("Shortest Distance:", g[stop])
                print("Total Energy Cost:", energy_cost[stop])
                print("\n")
                #print("Nodes expanded:", len(closed_list))
                return

            # For all the neighbors of the current node
            # (m= node number, weight= {distance, energy})
            for (child , weight) in self.get_neighbors(current):

                # Do not consider the node if it exceeds the energy constraint.
                if energy_cost[current] + weight[1] <= max_energy:

                    if child not in open_list and child not in closed_list:
                        # Adding in the neighbours of the parent
                        open_list.add(child)
                        # Noting that parent vertex
                        parent[child] = current
                        # Noting the accumulated distance
                        g[child] = g[current] + weight[0]
                        # Noting the accumulated energy cost
                        energy_cost[child] = energy_cost[current] + weight[1]

                    else:
                        # Check if there is another path to the child note that has a shorter path
                        if g[child] > g[current] + weight[0]:
                            # Noting the new parent vertex
                            parent[child] = current
                            # Noting the new accumulated distance
                            g[child] = g[current] + weight[0]
                            # Noting new accumulated distance
                            energy_cost[child] = energy_cost[current] + weight[1]

                            if child in closed_list:
                                closed_list.remove(child)
                                open_list.add(child)

            open_list.remove(current)
            closed_list.add(current)

            # Get first node from open list
            if len(open_list) > 0:
                current = list(open_list)[0]

        print('Path does not exist!')
        return None

#--------------------------------------------  MAIN  ------------------------------------------------

import json
import time
import sys

def run_task3():
    COORD_FILE = 'Coord.json'
    COST_FILE = 'Cost.json'
    G_FILE = 'G.json'
    COORD_FILE = 'Coord.json'
    DIST_FILE = 'Dist.json'
    COMBINED_FILE = 'New_Adjlist_task3.json'

    max_energy = 287932
    total_v = 264346
    total_e = 730100

    # To Generate the new list
    def regenerate_adjlist(data_g, data_dist, data_cost):
        new_adjlist = {}
        for key in data_g.keys():
            final = []
            for neighbour in data_g[key]:
                details = [neighbour, (data_dist[str(key+","+neighbour)],data_cost[str(key+","+neighbour)])]
                final.append(details)
            new_adjlist[key]= final
        f = open("data/New_Adjlist_task3.json", "w")
        json.dump(new_adjlist, f)
        f.close()


    def read_new_json_data():

        with open(COMBINED_FILE) as json_file:
            data_combined = json.load(json_file)

        with open(COORD_FILE) as json_file:
            data_coord = json.load(json_file)

        return data_combined, data_coord


    data_combined, data_coord = read_new_json_data()
    #print("Running Task 3 - A* Search Algorithm...")
    again = 'y'
    while (again == 'y'):
        start = input("Please enter the start node:")
        stop = input("Please enter the end node:")
        start.strip(" ")
        stop.strip(" ")
        graph1 = Graph(data_combined, data_coord)
        #print("Calculating path from: ", start , "->", stop, ", with", max_energy, "energy constraint...")
        time_start = time.time()
        graph1.a_star(start, stop, max_energy)
        time_end = time.time()
        #print(f"Runtime of the program is {time_end - time_start}")
        again = input("Run again? [y/n]")
        again = again.lower()




