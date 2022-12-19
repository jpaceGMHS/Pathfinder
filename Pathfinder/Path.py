import Grid
import pygame as py

class Node:
    def __init__(self):
        self.previous = None
        self.distance = 999
        self.Connected_Nodes = []
        self.weight = 1
    
    
class Dijkstra:
    def __init__(self, maze):
        self.maze = maze
        self.maze.Get_Start().distance = 0
        self.unchecked = []
        self.checked = []
        self.solution = []
        self.Preload_Connections()
        self.Preload_Unchecked()
    
    def Find_Connection(self, current, location):
        test_Node = self.maze.Get_Cell_byPosition(location)
        if test_Node:
            if test_Node.State != Grid.State.WALL:
                
                # START HERE
                current.Connected_Nodes.append(test_Node)
    
    def Preload_Connections(self):
        for ii in range(0, self.maze.Dimension):
            for jj in range(0, self.maze.Dimension):
                current = self.maze.Get_Cell_byPosition((jj, ii))
                if current.State != Grid.State.WALL:
                #Test Left
                    self.Find_Connection(current, (jj-1, ii))
                    self.Find_Connection(current, (jj+1, ii))
                    self.Find_Connection(current, (jj, ii-1))
                    self.Find_Connection(current, (jj, ii+1))
                    
    def Preload_Unchecked(self):
        self.unchecked = sum(self.maze.Cells, [])
        self.Sort_Unchecked()
        
    def Sort_Unchecked(self):
        self.unchecked.sort(key=lambda x: x.distance, reverse=False)
        
    def Step(self):
        current = self.unchecked[0]
        self.unchecked.remove(current)
        if current.State == Grid.State.STOP:
            self.checked.append(current)
            return True
        for adjacent in current.Connected_Nodes:
            val = current.distance + adjacent.weight
            if val < adjacent.distance:
                adjacent.previous = current
                adjacent.distance = val
        self.checked.append(current)
        current.State = Grid.State.SEARCHED
        self.Sort_Unchecked()
        return False
    
    
    def Solve(self):
        while not self.Step():
            pass
        
        current = self.maze.Get_Stop()
        while current:
            self.solution.append(current)
            current.State = Grid.State.PATH
            current = current.previous
        self.solution.reverse()
    
if __name__ == "__main__":
    screen = py.display.set_mode((500, 500))
    m = Grid.Grid(screen, 5)
    d = Dijkstra(m)
    d.Preload_Connections()
    
    
    
    
    
    
    