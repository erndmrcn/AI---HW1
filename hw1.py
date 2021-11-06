###################################
# Author:   Eren Demircan - 2237246
# Created:  06.11.2021
# CEng462 - AI
# Homework1 - Search Problems


# data structures that will be used through this assignment
def initialize():
    return []


def enqueue(queue, index, value):
    queue.insert(index, value)


def dequeue(queue, index):
    return queue.pop(index)


# FIFO Queue
# LIFO Queue - Stack
# Priority Queue

# Node for tree search
class Node:
    state = str("")
    parent = None
    action = None
    pathCost = None


# read inputs
def read(fileName):
    with open(fileName, 'r') as f:
        line = f.readline()
        startNode = line[:-1]

        line = f.readline()
        targetNode = line[:-1]

        print("StartNode = ", startNode)
        print("TargetNode = ", targetNode)

        cities = []
        while line:
            line = f.readline()[:-1]
            cities.append(line)

        cities.pop(-1)
        print(cities)
    f.close()


# write outputs
def write():
    print()


# tree-search
def treeSearch():
    return


# Breadth-First Search
def BFS():
    return


# Depth-Limited Search
def DLS():
    return


# Iterative Deepening Depth-First Search
def IDDFS():
    return


def UCS():
    return


read("example2.txt")
