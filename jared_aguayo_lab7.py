import numpy as np
import random

"""
Code by: Jared Aguayo
Last Modified: 12/3/19
Lab 7 
Professor: Olac Fuentes
TA: Anindita Nath 
"""

#Create an empty path array and add vertex 0 to it. Add other vertices, starting from the vertex 1. 
#Before adding a vertex, check for whether it is adjacent to the previously added vertex and not already added.
#If we find such a vertex, we add the vertex as part of the solution. 
#If we do not find a vertex then we return false
class DSF:
    # Constructor
    def __init__(self, sets):
        # Creates forest with 'sets' root nodes
        self.parent = np.zeros(sets,dtype=int)-1
      
    def find(self,i):
        # Returns root of tree that i belongs to
        if self.parent[i]<0:
            return i
        return self.find(self.parent[i])

    def union(self,i,j):
        # Makes root of j's tree point to root of i's tree if they are different
        # Return 1 if a parent reference was changed, 0 otherwise
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            return 1
        return 0
    
    
def connected_components(g):
    vertices = len(g)
    components = vertices
    s = DSF(vertices )
    for v in range(vertices):
        for edge in g[v]:
            components -= s.union(v,edge)
    return components


def graph(vertices, edges, duplicate=True):
    g = [ [] for i in range(vertices) ]
    n=0
    while n<edges:
        s = random.randint(0, vertices-1)
        d = random.randint(0, vertices-1)
        if s<d and d not in g[s]:
            g[s].append(d)
            if duplicate:
                g[d].append(s)
            n+=1
    for i in range(len(g)):
        g[i].sort()
    return g

def backtracking_hamiltonian(g):
    return 0


def randomized_hamiltonian(v,e,tries=3):
    for i in range(tries):
        g = graph(v,e)
        isHamiltonian = hamiltonian_cycle(g)
        print('Random Graph Being Checked')
        print(g)
        print(isHamiltonian)
        print('\n')
            
            
def hamiltonian_cycle(g):
    cc = connected_components(g)
    
    for i in range(len(g)):
        in_degrees = 0 
        in_degrees = in_degree(g,i)
        if in_degrees == 2 and cc == 1:
            continue
        else:
            return False
    return True


def in_degree(g,v):
    count = 0
    for i in range(len(g)):
        for edge in g[i]:
           if edge ==  v:
               count+=1
    return count


def edit_distance(s1,s2):
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[0,:] = np.arange(len(s2)+1)
    d[:,0] = np.arange(len(s1)+1)
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] ==s2[j-1]:
                d[i,j] =d[i-1,j-1]
            else:
                can_swap = vowel_or_consonant(s1[i-1],s2[j-1])
                #swap may be in the corner of the three you check
                if can_swap == True:
                    n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                    d[i,j] = min(n)+1
                else :
                    n = [d[i,j-1],d[i-1,j]]
                    d[i,j] = min(n)+1
    return d[-1,-1]


def vowel_or_consonant(s1,s2):
    s1_vowel = False
    s2_vowel = False
    
    vowels = ['a','e','i','o','u']
        
    for i in range(len(vowels)):
        if s1 == vowels[i]:
            s1_vowel = True
        if s2 == vowels[i]:
            s2_vowel = True
            
    if s1_vowel == s2_vowel:
        return True
    else :
        return False
    

class Graph:
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
        
        
    def display(self):
        print(self.am)
    
    
def check_adjacents(g, v, pos, path): 
        if g.am[ path[pos-1] ][v] == -1: 
            return False
  
        for vertex in path: 
            if vertex == v: 
                return False
  
        return True
  
def backtracking_ham(g, path, pos): 
        if pos == len(g.am): 

            if g.am[ path[pos-1] ][ path[0] ] == 1: 
                return True
            else: 
                return False
  
        for v in range(1,len(g.am)): 
            if check_adjacents(g,v, pos, path) == True: 
                path[pos] = v 
                
                if backtracking_ham(g,path, pos+1) == True: 
                    return True
                path[pos] = -1
  
        return False
  
def ham_cycle(g):
    path = [-1] * len(g.am)
  
    path[0] = 0

    if backtracking_ham(g,path,1) == False: 
        return False
    return True  


if __name__ == "__main__": 
    
    vowels = ['a','e','i','o','u']
    print('Altered Edit Distance')
    print(edit_distance('sand', 'sound'))
    print('\n')

    randomized_hamiltonian(4,4)
    
    
    g = Graph(5)
    g.insert_edge(0,1)
    g.insert_edge(0,3)
    g.insert_edge(1,0)
    g.insert_edge(1,2)
    g.insert_edge(1,3)
    g.insert_edge(1,4)
    g.insert_edge(2,1)
    g.insert_edge(2,4)
    g.insert_edge(3,0)
    g.insert_edge(3,1)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.insert_edge(4,2)

    print('Backtracking Hamiltonian Cycle using AM')
    g.display()
    print(ham_cycle(g))
    print('\n')
    
    g = Graph(5)
    g.insert_edge(0,1)
    g.insert_edge(0,3)
    g.insert_edge(1,0)
    g.insert_edge(1,2)
    g.insert_edge(1,3)
    g.insert_edge(1,4)
    g.insert_edge(2,1)
    g.insert_edge(2,4)
    g.insert_edge(3,0)
    g.insert_edge(3,1)
    g.insert_edge(4,1)
    g.insert_edge(4,2)
    
    g.display()
    print(ham_cycle(g))
    