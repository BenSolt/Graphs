from graph import Graph
from util import Queue, Stack


def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    q.enqueue([starting_node])
    visited = set()
    paths = list()

    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]

        if current_node not in visited:
            visited.add(current_node)
    
            for n in ancestors:
                
                if current_node == n[1]:
                    next_path = list(path)
                    # add the next node to the end 
                    next_path.append(n[0])
                    # add next_path to the queue
                    q.enqueue(next_path)
                    # add the next_path to paths
                    paths.append(next_path)
                    
    #If input individual has no parents, return -1.
    if current_node == starting_node:
        return -1
    # if multiple paths
    elif len(paths) > 1:
        last_path = paths[-1]

        for path in paths:
            if len(path) == len(last_path) and path[-1] < last_path[-1]:
                current_node = path[-1]
                
        return current_node
    else: 
        return current_node
