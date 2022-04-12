from collections import defaultdict 
class BfsTraverser: 
  # Constructor 
  def __init__(self): 
    self.visited = []
    self.end_search = False
  def BFS(self,graph, start_node, goal_node):
    queue = []
    queue.append(start_node)
    
    self.visited.append(start_node)
    while queue and not self.end_search: 
      # Dequeue a vertex from 
      s = queue.pop(0)          
      for i in list(graph[s]):
        if i not in self.visited:
          print ("Command; walk to " ,i, " Junction", end = "\n")
          if i is goal_node:
            print("We have reached the  ",i," as the final destination")
            self.visited.append(i)
            self.end_search = True
            break
          else:
            queue.append(i)
            self.visited.append(i)

