# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:30:13 2020

@author: Asus
"""

#This class represents a directed graph using adjacency matrix representation 

def zeros_list(n):
    temp = []
    for i in range(n):
        temp.append(0)
    return temp
def last_num_zero(n):
    temp = []
    for i in range(n - 1):
        temp.append(0)
    temp.append(1)
    return temp


def fuck_this(m,n):
    temp = []
    for i in range(m+1):
        temp.append(0)
    for j in range(n):
        temp.append(1)
    temp.append(0)
    return temp

class Graph: 
   
    def __init__(self,graph): 
        self.graph = graph # residual graph 
        self. ROW = len(graph) 
        #self.COL = len(gr[0]) 
          
   
    '''Returns true if there is a path from source 's' to sink 't' in 
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.ROW) 
          
        # Create a queue for BFS 
        queue=[] 
          
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
           
         # Standard BFS Loop 
        while queue: 
  
            #Dequeue a vertex from queue and print it 
            u = queue.pop(0) 
          
            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
  
        # If we reached sink in BFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False
              
      
    # Returns tne maximum flow from s to t in the given graph 
    def FordFulkerson(self, source, sink): 
  
        # This array is filled by BFS and to store path 
        parent = [-1]*(self.ROW) 
  
        max_flow = 0 # There is no flow initially 
  
        # Augment the flow while there is path from source to sink 
        while self.BFS(source, sink, parent) : 
  
            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            # Add path flow to overall flow 
            max_flow +=  path_flow 
  
            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
  
        return max_flow 


info = list(map(int, input().split()))
n, m = info[0], info[1]
number = int(input())
data = []
for i in range(number):
    data.append(list(map(int, input().split())))


graph = []
temp = zeros_list(n+m+2)
for i in range(1, m+1):
    temp[i] = 1

graph.append(temp)
for i in range(m):
    graph.append(fuck_this(m,n))

for i in range(n):
    graph.append(last_num_zero(n+m+2))

graph.append(zeros_list(n+m+2))


for i in range(len(data)):
    graph[data[i][1]+1][1+m+data[i][0]] = 0
g = Graph(graph) 
  
source = 0; sink = n+m+1
   
print (int(g.FordFulkerson(source, sink)))