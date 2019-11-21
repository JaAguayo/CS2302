"""
Code by: Jared Aguayo
Last Modified: 11/14/19
Lab 6 Graphs (chicken, fox, and grain)
Professor Fuentes
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


"""
Adjacency list representation of graphs
"""

class EdgeAL:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight
        
class GraphAL:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'
        
    def insert_edge(self,source,dest,weight=1):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        if weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(EdgeAL(dest,weight)) 
    
    def delete_edge_(self,source,dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i+=1    
        return False
    
    def delete_edge(self,source,dest):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            deleted = self.delete_edge_(source,dest)
            if not self.directed:
                deleted = self.delete_edge_(dest,source)
        if not deleted:        
            print('Error, edge to delete not found')      
            
    def display(self):
        print('[',end=' ')
        for i in range(len(self.al)):
            print('[',end='')
            for edge in self.al[i]:
                print('('+str(edge.dest)+','+str(edge.weight)+')',end='')
            print(']',end=' ')    
        print(']')   
     
    def draw(self):
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.al)):
            for edge in self.al[i]:
                d,w = edge.dest, edge.weight
                if self.directed or d>i:
                    x = np.linspace(i*scale,d*scale)
                    x0 = np.linspace(i*scale,d*scale,num=5)
                    diff = np.abs(d-i)
                    if diff == 1:
                        y0 = [0,0,0,0,0]
                    else:
                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
                    f = interp1d(x0, y0, kind='cubic')
                    y = f(x)
                    s = np.sign(i-d)
                    ax.plot(x,s*y,linewidth=1,color='k')
                    if self.directed:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.plot(xd,yd,linewidth=1,color='k')
                    if self.weighted:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
            ax.text(i*scale,0, str(i), size=10,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off') 
        ax.set_aspect(1.0)
        
    def as_EL(self):
        print('Edge List Representation')
        for i in range (len(self.al)):
            for edge in self.al[i]:
                print('(',i,',',edge.dest,',',edge.weight,')')
    
    def as_AM(self):
        am = np.zeros((len(g.al),len(g.al)),dtype=int)-1
        for i in range(len(self.al)):
            for edge in self.al[i]:
                am[i][edge.dest] = edge.weight
        print(am)
    
    def as_AL(self):
        return self.display()

        
"""
Adjacency Matrix representation of graphs
"""
        
class GraphAM:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.am = np.zeros((vertices,vertices),dtype=int)-1
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AM'
        
    def insert_edge(self,source,dest,weight=1):
        if source >= len(self.am) or dest>=len(self.am) or source <0 or dest<0:
            print('Error, vertex number out of range')
        elif weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.am[source][dest] = weight
            if not self.directed:
                self.am[dest][source] = weight
        
    def delete_edge(self,source,dest):
        if source >= len(self.am) or dest>=len(self.am) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            self.am[source][dest] = -1
            if not self.directed:
                self.am[dest][source] = -1
        
    def display(self):
        print(self.am)
        
    def as_EL(self):
        for i in range (len(self.am)):
            for j in range(len(self.am)):
                if self.am[i][j] != -1:
                    print('(',i,',',j,',',1,')')
    
    def as_AM(self):
        return self.display()
    
    def as_AL(self):
        L = [[]for i in range(len(self.am))]
        for i in range (len(self.am)):
            for j in range(len(self.am)):
                if self.am[i][j] != -1:
                    L[i].append(EdgeAL(j,1))
        print('[',end='')
        for i in range(len(L)):
            print('[',end='')
            for edge in L[i]:
                print('('+str(edge.dest)+','+str(edge.weight)+')',end='')
            print(']',end=' ')    
        print(']') 

"""
Edge list representation of graphs
"""

class EdgeEL:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class GraphEL:
    # Constructor
    def __init__(self,  vertices, weighted=False, directed = False):
        self.vertices = vertices
        self.el = []
        self.weighted = weighted
        self.directed = directed
        self.representation = 'EL'
        
    def insert_edge(self,source,dest,weight=1):
        if weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.el.append(EdgeEL(source,dest,weight)) 
            
    def delete_edge_(self,source,dest):
        i = 0
        for edge in self.el:
            if edge.dest == dest:
                self.el.pop(i)
                return True
            i+=1    
        return False
    
    def delete_edge(self,source,dest):
        if source >= len(self.el) or dest>=len(self.el) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            deleted = self.delete_edge_(source,dest)
            
        if not deleted:        
            print('Error, edge to delete not found') 
                
    def display(self):
        for edge in self.el:
            print('(',edge.source,',',edge.dest,',',edge.weight,')')
            
    def as_EL(self):
        return self.display
    
    def as_AM(self):
        am = np.zeros((self.vertices,self.vertices),dtype=int)-1
        for edge in self.el:
            am[edge.source][edge.dest] = edge.weight
        print(am)
    
    def as_AL(self):
        L = [[]for i in range(self.vertices)]
        for edge in self.el:
            L[edge.source].append(EdgeAL(edge.dest,edge.weight))
        
        print('[',end='')
        for i in range(len(L)):
            print('[',end='')
            for edge in L[i]:
                print('('+str(edge.dest)+','+str(edge.weight)+')',end='')
            print(']',end=' ')    
        print(']') 
            
#------------------------------------------------------------------

def BFS(g,s):
    Q = []
    visited = [False]*len(g.al)
    path = [-1]*len(g.al)
    
    Q.append(s)
    visited[s] = True
    
    while Q:
        v = Q.pop(0)
        
        for edge in g.al[v]:
            if visited[edge.dest] == False:
                Q.append(edge.dest)
                visited[edge.dest] = True
                path[edge.dest] = v
    return path

def DFS(g,s):
    stack = []
    visited = [False]*len(g.al)
    path = [-1]*len(g.al)
    
    stack.append(s)
    
    while stack:
        v = stack.pop()
        
        if visited[v] == False:
            visited[v] = True
            
            for edge in g.al[v]:
                if visited[edge.dest] == False:
                    stack.append(edge.dest)
                    path[edge.dest] = v
    
    return path      

def valid_graph_points(L):
    valid_points = []
    invalid_points = []
    for i in range(len(L)):
        if (L[i][0] == L[i][1] and L[i][3] != L[i][0]) or (L[i][1] == L[i][2] and L[i][3] != L[i][1]):
            invalid_points.append(L[i])
        else :
            valid_points.append(L[i])
    return valid_points,invalid_points

def create_edges(L):
    g = GraphAL(16)
    
    for i in range(len(L)):
        for j in range(len(L)):
            
            check = int(L[i],2)
            
            bit_diff = dif(L[i],L[j])
            
            if len(bit_diff) < 3 and len(bit_diff) > 0:
                if L[j][3] != L[i][3]:
                    decimal = int(L[j],2)
                    g.insert_edge(check,decimal)
    return g        

def dif(bin1, bin2):
    return [i for i in range(len(bin1)) if bin1[i] != bin2[i]]

def path_list(path,dest):
    if path[dest] != -1:
        path_list(path,path[dest])
        print('-->',dest,end = '')
    else:
        print('-->',dest,end = '')
        
        
if __name__ == "__main__":   
    print('---------------------------------------------')
    L = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    a,b = valid_graph_points(L)
    
    print('Valid Moves')
    print(a)
    print('\n')
    print('Invalid Moves')
    print(b)
    
    g = create_edges(a)
    
    print('\n')
    print('Fox,Chicken,Grain,Person Graph')
    
    g.display()
    
    print('\n')
    
    g.as_EL()
    
    print('\n')
    
    g.as_AM()
    g.draw()
    
    print('\n')
    print('Breadth Search Path')
    
    BFSpath = BFS(g,0)
    path_list(BFSpath,15)
    
    print('\n')
    print('Depth Search Path')
    
    DFSpath = DFS(g,0)
    path_list(DFSpath,15)
    
    print('\n')
    print('Delete Edge: 0,5')
    
    g.delete_edge_(0,5)
    g.display()
    
    print('\n')
    print('Insert Edge: 0,5')
    
    g.insert_edge(0,5)
    g.display()
    
    print('\n')

    print('---------------------------------------------')
    
    print('---------------------------------------------')
    print('Adjacency Matrix')
    g = GraphAM(6)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    #g.draw()
    print('\n')
    print('Delete AM')
    
    g.delete_edge(1,2)
    g.display()
    
    print('\n')
    
    g.as_EL()
    
    print('\n')
    
    g.as_AL()
    
    print('\n')
    print('---------------------------------------------')
    
    print('---------------------------------------------')
    print('Edge List')
    g = GraphEL(6)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()

    print('\n')
    print('Delete EL')
    
    g.delete_edge(1,2)
    g.display()
    
    print('\n')
    
    g.as_AM()
    
    print('\n')
    
    g.as_AL()
    
    print('\n')
    print('---------------------------------------------')