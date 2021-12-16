
from queue import PriorityQueue
from collections import defaultdict
 

# Helper method to build the graph from input matrix
def build_undirected_graph(edges, n_nodes):
    result_graph = defaultdict(list)

    # Add existing edges to the graph
    for edge in edges:
        result_graph[edge[0]].append((edge[1], edge[2]))
        result_graph[edge[1]].append((edge[0], edge[2]))

    # Account for disconnnected nodes. 
    for i in range(1, n_nodes + 1):
        if i not in result_graph:
            result_graph[i] = []

    return result_graph


# Helper method implementing dijkstra.
def dijkstra_implementation(graph, starting_vertex):

    priority_queue = PriorityQueue()
    priority_queue.put((0, starting_vertex))

    # Weight dictionary
    D_algo = {}

    # Set all edge weight to infinity. 
    for vertex in range(1, len(graph)+1):
        D_algo[vertex] = float('INF')

    # Set the edge of the starting node to zero. 
    D_algo[starting_vertex]  = 0


    # Initialize visited set to keep track of visited nodes. 
    visited_set = set()


    while not priority_queue.empty():
        # Get the node with least cost
        (c_cost, c_vertex) = priority_queue.get()


        visited_set.add(c_vertex)

        # Update the cost of connected nodes
        for k in graph[c_vertex]:
            if k[0] not in visited_set:
                new_cost = k[1] + c_cost

                if new_cost < D_algo[k[0]]:
                    D_algo[k[0]] = new_cost
                    priority_queue.put((new_cost, k[0]))


    return D_algo
 
def shortestReach(n_node, g_edges, s_node):
    new_graph = build_undirected_graph(edges=g_edges, n_nodes=n_node)

    Djkt = dijkstra_implementation(new_graph, s_node)  

    g_list = []
    for i in range(1, len(Djkt)+1):
        if i != s_node:
            g_list.append(Djkt[i])
    mylist = []
    for k in g_list:
        if k == float('INF'):
            mylist.append(-1)
        else:
            mylist.append(k) 

    return mylist


print(shortestReach(4, [[1,2,24], [1,3,3], [1,4,20], [3,4,12]], 1))
print(shortestReach(5, [[1,2,5], [2,3,6], [3,4,2], [1,3,15]], 1))