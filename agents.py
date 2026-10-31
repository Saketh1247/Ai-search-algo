import heapq

from .ModelTemplate import ModelTemplate
from .Map import Map
from .Nodes import Nodes


class BFS(ModelTemplate):
    def explore(self):
        self.visited_nodes.append(self.Map.start_node)
        queue=[self.Map.start_node]
        while queue:
            current_node=queue.pop(0)
            if current_node.city==self.Map.goal:
                print("Goal Reached")
                return current_node
            else:
                for i in self.Map.neighbours(current_node):
                    if i.city not in [x.city for x in self.visited_nodes]:
                        self.visited_nodes.append(i)
                        queue.append(i)
        return -1

class DFS(ModelTemplate):
    def explore(self):
            self.visited_nodes.append(self.Map.start_node)
            stack=[self.Map.start_node]
            while stack:
                current_node=stack.pop()
                if current_node.city==self.Map.goal:
                    print("Goal Reached")
                    return current_node
                else:
                    for i in self.Map.neighbours(current_node)[::-1]:
                        if i.city not in [x.city for x in self.visited_nodes]:
                            self.visited_nodes.append(i)
                            stack.append(i)
            return -1

class UCS(ModelTemplate):
    def explore(self):
        self.visited_nodes.append(self.Map.start_node)
        counter=0
        frontier=[(0, counter, self.Map.start_node)]
        finalized=set()
        while frontier:
            cost, _, current_node = heapq.heappop(frontier)
            if current_node.city in finalized:
                continue
            finalized.add(current_node.city)
            if current_node.city==self.Map.goal:
                print("Goal Reached")
                return current_node
            for i in self.Map.neighbours(current_node, current_node.current_cost):
                if i.city not in finalized:
                    self.visited_nodes.append(i)
                    counter+=1
                    heapq.heappush(frontier, (i.current_cost, counter, i))
        return -1

class GBFS(ModelTemplate):
    def explore(self):
        self.visited_nodes.append(self.Map.start_node)
        counter=0
        frontier=[(0, counter, self.Map.start_node)]
        finalized=set()
        while frontier:
            _, _, current_node = heapq.heappop(frontier)
            if current_node.city in finalized:
                continue
            finalized.add(current_node.city)
            if current_node.city==self.Map.goal:
                print("Goal Reached")
                return current_node
            for i in self.Map.neighbours(current_node):
                if i.city not in finalized:
                    self.visited_nodes.append(i)
                    counter+=1
                    heapq.heappush(frontier, (i.heuristic_cost, counter, i))
        return -1

class A_star(ModelTemplate):
    def explore(self):
        self.visited_nodes.append(self.Map.start_node)
        counter=0
        frontier=[(0, counter, self.Map.start_node)]
        finalized=set()
        while frontier:
            _, _, current_node = heapq.heappop(frontier)
            if current_node.city in finalized:
                continue
            finalized.add(current_node.city)
            if current_node.city==self.Map.goal:
                print("Goal Reached")
                return current_node
            for i in self.Map.neighbours(current_node, current_node.current_cost):
                if i.city not in finalized:
                    self.visited_nodes.append(i)
                    counter+=1
                    total_cost=i.current_cost + i.heuristic_cost
                    heapq.heappush(frontier, (total_cost, counter, i))
        return -1