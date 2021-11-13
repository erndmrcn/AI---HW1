###################################
# Author:   Eren Demircan - 2237246
# Created:  06.11.2021
# CEng462 - AI
# Homework1 - Search Problems


# data structures and variables that will be used through this assignment
city1 = []
city2 = []
costs = []

# Node for tree search
class Node:

    def __init__(self, state, parent, cost):
        # node state
        self.state = state
        # parent node pointer - None for root
        self.parent = parent
        # path cost
        self.cost = cost
        

# read inputs
def read(fileName):

    global startNode, targetNode

    with open(fileName, 'r') as f:
        line = f.readline()
        startNode = line[:-1]

        line = f.readline()
        targetNode = line[:-1]

        cities = []
        while line:
            line = f.readline()[:-1]
            cities.append(line)

        cities.pop(-1)

        for city in cities:
            result = city.split(' ')
            city1.append(str(result[0]))
            city2.append(str(result[1]))
            costs.append(int(result[2]))
        
    f.close()


# finding next state given current state
# multiple paths for the same nodes accepted and both added -> additional computation
# one can go to the node where he has come from -> infinite loop
def expand(state):

    global children 
    children = []

    # find the first state that can be reached from the current state
    # for both directions
    for i in range(0, len(city1)):
        if city1[i] == state.state: 
            temp = Node(city2[i], state, state.cost + costs[i])
            children.append(temp)
        elif city2[i] == state.state:
            temp = Node(city1[i], state, state.cost + costs[i])
            children.append(temp)

    return children


# find the path to the result Node 
def printPath(node):
    global bfs_depth
    result = []
    result.append(node.state)
    bfs_depth = 0

    while node.parent != None:
        bfs_depth += 1
        result.append(node.parent.state)
        node = node.parent
    
    return result


# Breadth-First Search
def BFS():

    root = Node(startNode, None, 0)
    
    # list of nodes that are to be expanded
    frontier = []
    frontier.append(root)

    result = []
    processed = []

    while frontier:

        # FIFO Queue
        currentNode = frontier[0]
        frontier = frontier[1:]
        processed.append(currentNode.state)

        if  currentNode.state == targetNode:
            result = printPath(currentNode)
            return result, processed

        frontier.extend(expand(currentNode))
    
    return None
    

def recursiveDLS(result, processed, root, depthLimit):

    processed.append(root.state)
    result.append(root.state)
    frontier = []

    if root.state == targetNode:
        return result, processed, len(result) - 1
    
    if  depthLimit == 0:
        return None
    
    frontier = expand(root)
    for item in frontier:
        if recursiveDLS(result, processed, item, depthLimit-1):
            return result, processed, len(result) - 1        
        result.pop()
    return None 


# Depth-Limited Search
def DLS(depthLimit):

    result = []
    processed = []
    root = Node(startNode, None, 0)

    # starting from the 0 depth to max_depth_limit
    # if a path with depth less than the max_depth_limit
    # can be found, return that path -> eliminates redundant paths
    for i in range(0, depthLimit+1):
        if recursiveDLS(result, processed, root, i):
            return result, processed, len(result) - 1
        else:
            result.pop()

    return None

# Iterative Deepening Depth-First Search
def IDDFS(maxLimit):
    # starting from 0 try each depth limit
    for i in range(maxLimit):
        result = DLS(maxLimit)
        if result != None:
            return result


# sort helper
def getCost(e):
    return e.cost


# sorting
# preparing for priority queue
def sortFrontier(frontier):

    if len(frontier) <= 1:
        return frontier
    
    return frontier.sort(reverse=False, key=getCost)
    

# Uniform-cost search
def UCS():

    # first node to be expanded
    frontier = [Node(startNode, None, 0)]

    result = []
    processed = []

    while frontier:
        # sort nodes that are to be expanded
        # comparing their costs
        sortFrontier(frontier)

        # Priority Queue
        # take node with min cost
        currentNode = frontier[0]
        frontier = frontier[1:]

        processed.append(currentNode.state)

        if  currentNode.state == targetNode:
            result = printPath(currentNode)
            return result, processed, currentNode.cost

        frontier.extend(expand(currentNode))

    return None



def UnInformedSearch(method_name, problem_fileName, maximum_depth_limit):

    if  method_name == "BFS":

        read(problem_fileName)
        result, processed = BFS()
        
        city1.clear()
        city2.clear()
        costs.clear()
        startNode = ""
        targetNode = "" 
        result = result[::-1]

        return result, processed, bfs_depth

    elif method_name == "DLS":

        read(problem_fileName)
        result = DLS(maximum_depth_limit)

        city1.clear()
        city2.clear()
        costs.clear()
        startNode = ""
        targetNode = "" 

        return result

    elif method_name == "IDDFS":

        read(problem_fileName)
        result = IDDFS(maximum_depth_limit)

        city1.clear()
        city2.clear()
        costs.clear()
        startNode = ""
        targetNode = "" 
    
        return result

    elif method_name == "UCS":
        read(problem_fileName)
        result, processed, cost = UCS()
        
        city1.clear()
        city2.clear()
        costs.clear()
        startNode = ""
        targetNode = "" 
        result = result[::-1]
           
        return result, processed, bfs_depth, cost
