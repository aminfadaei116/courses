# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 23:33:48 2019

@author: Asus
"""

class Graph :
    def __init__(self) :
        self.nodes = {}
    
    def add_node(self, n) :
        if n in self.nodes :
            return
        self.nodes[n] = {}
        
    def add_yal(self, n, m) :
        w = abs(n - m)
        self.nodes[n][m] = w
        self.nodes[m][n] = w
        
    def dijkstra(self, s, t) :
        S = []
        ready_yals_w = [0]
        ready_yals_n = [s]
        while True :
            index = ready_yals_w.index(min(ready_yals_w))
            new = ready_yals_n[index]
            w = ready_yals_w[index]
            if new == t :
                return w
            S.append(new)
            del ready_yals_n[index]
            del ready_yals_w[index]
            for other in self.nodes[new] :
                if other in S :
                    continue
                elif other in ready_yals_n :
                    other_index = ready_yals_n.index(other)
                    if w + self.nodes[new][other] < ready_yals_w[other_index] :
                        ready_yals_w[other_index] = w + self.nodes[new][other]
                else :
                    ready_yals_n.append(other)
                    ready_yals_w.append(w + self.nodes[new][other])

def main():
    info = list(map(int, input().split()))
    n, s, t = info[0], info[1], info[2]
    graph = Graph()
    for i in range(n):
        elev = list(map(int, input().split()))[1:]
        for j,e in enumerate(elev):
            graph.add_node(e)
            for k in range(j):
                graph.add_yal(e, elev[k])
    print(graph.dijkstra(s,t))

if __name__ == '__main__':
    main()
    