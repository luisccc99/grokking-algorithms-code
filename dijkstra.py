'''Dijkstra's algorithm is used to calculate the shortest path
for a weighted graph.
It only works when all the weights are positive.
'''

import math

# nested dictionary to represent vertices and the cost of their edges
graph = {}
graph['start'] = {}
graph['start']['A'] = 6
graph['start']['B'] = 2
graph['A'] = {}
graph['A']['fin'] = 1
graph['B'] = {}
graph['B']['A'] = 3
graph['B']['fin'] = 5
graph['fin'] = {}

# initial cots (how long it takes to get to a node)
costs = {}
costs['A'] = 6
costs['B'] = 2
costs['fin'] = math.inf # we don't know (yet) how long it takes to the fin

# keep track of parents to calculate the final path
parents = {}
parents['A'] = 'start'
parents['B'] = 'start'
parents['fin'] = None

# to not process nodes more than once
processed = []

# find lowest cost that hasn't been processed
# a priority queue can be used as well
def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node 
    return lowest_cost_node

# while there are nodes to process
# find the 'cheapest' node (the one with the lowest cost)
# update costs for its neighbors
# if any of the neighbor's costs were updated, update the parents too
# mark the node as processed
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

# display final path, going from finish to start (following parents)
traversed = []
node = parents['fin']
traversed.append('fin')
while node in parents:
    traversed.append(node)
    node = parents[node]
traversed.append('start')
traversed.reverse()
print(traversed)