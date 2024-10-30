#Assig
from collections import deque

graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

def dfs(graph, start):
    """Performs Depth-First Search on the graph starting from 'start' node."""
    visited = set()          
    stack = [start]          

    traversal = []           

    while stack:
        node = stack.pop()    
        if node not in visited:
            visited.add(node)         
            traversal.append(node)    

           
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal

def bfs(graph, start):
    """Performs Breadth-First Search on the graph starting from 'start' node."""
    visited = set()          
    queue = deque([start])   

    traversal = []            
    while queue:
        node = queue.popleft()    
        if node not in visited:
            visited.add(node)         
            traversal.append(node)    

            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal


if __name__ == "__main__":
    start_node = 2
    print("DFS Traversal starting from node", start_node, ":", dfs(graph, start_node))
    print("BFS Traversal starting from node", start_node, ":", bfs(graph, start_node))

