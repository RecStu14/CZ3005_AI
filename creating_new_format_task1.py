import json

#Opening JSON file - neighbours -> shows the nodes it is connected to
with open('G.json') as json_file:
    neighbours = json.load(json_file)

#Opening JSON file - distance -> shows the distance between each nodes
with open('Dist.json') as json_file:
    distances = json.load(json_file)

#Opening JSON file - cost -> shows the cost between each nodes
with open('Cost.json') as json_file:
    costs = json.load(json_file)

#initialising values 
num_nodes = len(neighbours)
num_edges = len(distances)

#Reformatting the list to contain the graph details in the following order
# {"node1" : [["node2", "dist1->2", "cost"],["node3", dist1->3, "cost"]]}

"""
 Fxn1 - create_dict 
    -> rationale: function to add the keys of the dictionary
    -> input: neighbours <dictionary> (read from G.json)
    -> output: graph <dictionary> that contains the information stored in the following format:
       {"node1" : [["node2", "dist1->2"],["node3", dist1->3]]}
"""
def create_dict(neighbours):
    #creating an empty dictionary to hold all the values 
    graph = {}
    neighbours_keys = list(neighbours.keys())

    #iterate over the list containing the keys of the G.json file
    for source_node in neighbours_keys:
        #adding all the connected nodes into a list
        connected_nodes = neighbours[source_node]

        #call the get_final_list that returns a list in the following format:
        # [connected_node, distance_to_the_connected_node]
        final_list = get_final_list(source_node,connected_nodes)

        #add the final list as the value to its corresponding source node
        graph[source_node] = final_list
        
    return graph


"""
Fxn2 - get_final_list
    -> rationale: function to create the final list of the format 
       [connected_node, distance_to_the_node_from_the_selected_node]
    -> input: source_node - which is the start node, connected_nodes <list> of corresponding connected nodes
    -> output: returns a 2D list [["node2", "dist1->2"],["node3", dist1->3]]
"""
def get_final_list(source_node, connected_nodes):
    #creating an empty list to store the sub-lists
    all_nodes_list = []

    #iterating through the list of connected nodes
    for node in connected_nodes:
        #creating a sub-list
        nodes_list = []

        #appending the first connected node
        nodes_list.append(node)

        #calling the get_distance function that retrieves the corresponding distance
        distance = get_distance(source_node, node)

        #append the distance to the sublist with the node name
        nodes_list.append(distance)

        #append the sublist to the final list
        all_nodes_list.append(nodes_list)

    return all_nodes_list

"""
Fxn3 - get_distance
    -> rationale: retrieves the corresponding distance from the source_node to the desired node
    -> input: source_node - which is the start node, node - which is the desired node
    -> output: distance <int> 
"""

def get_distance(source_node, node):
    key_value = str(source_node + "," + node)
    return distances[key_value] 

"""
Fxn 4 - get_cost
    -> rationale: retrieves the corresponding cost from the source_node to the desired node
    -> input: source_node - which is the start node, node - which is the desired node
    -> output: cost <int>
"""
def get_cost(source_node, node):
    key_value = str(source_node + ',' + node)
    return costs[key_value]

"""
Fxn5 - get_keys
    -> rationale: a getter function to facilitate the output the keys of the G.json and Dist.json across python files
    -> input: tag <str> - which asks indicates either neighbours keys or distances keys
    -> output: keys of either the G.json or Dist.json <list>
"""

def get_keys(tag):
    if tag == 'neighbours':
        return list(neighbours.keys())
    elif tag == 'distances':
        return list(distances.keys())
    elif tag == 'costs':
        return list(costs.keys())

#creating the dictionary graph
graph = create_dict(neighbours)














