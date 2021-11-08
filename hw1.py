###################################
# Author:   Eren Demircan - 2237246
# Created:  06.11.2021
# CEng462 - AI
# Homework1 - Search Problems


# data structures that will be used through this assignment

city1 = []
city2 = []
costs = []
global totalCost

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


def expand(state):
    children = []
    for i in range(0, len(city1)):
        if city1[i] == state.state: 
            temp = Node(city2[i], state, state.cost + costs[i])
            children.append(temp)
        elif city2[i] == state.state:
            temp = Node(city1[i], state, state.cost + costs[i])
            children.append(temp)

    return children


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
    frontier = []
    frontier.append(root)
    result = []
    processed = []
    explored = []

    while frontier:
        currentNode = frontier[0]
        frontier = frontier[1:]
        processed.append(currentNode.state)

        if  currentNode.state == targetNode:
            result = printPath(currentNode)
            return result, processed

        frontier.extend(expand(currentNode))
    
    return None


# Depth-Limited Search
def DLS():
    return


# Iterative Deepening Depth-First Search
def IDDFS():
    return


def getCost(e):
    return e.cost


def sortFrontier(frontier):
    if len(frontier) <= 1:
        return frontier
    
    return frontier.sort(reverse=False, key=getCost)
    

def UCS():
    frontier = [Node(startNode, None, 0)]
    result = []
    processed = []

    while frontier:
        sortFrontier(frontier)
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

        print(len(processed))  
        return result, processed, bfs_depth

    elif method_name == "DLS":
        DLS()
    elif method_name == "IDDFS":
        IDDFS()
    elif method_name == "UCS":
        read(problem_fileName)
        result, processed, cost= UCS()
        
        city1.clear()
        city2.clear()
        costs.clear()
        startNode = ""
        targetNode = "" 
        result = result[::-1]
           
        print(len(processed))  
        return result, processed, cost, bfs_depth
