import numpy as np
from operator import itemgetter,attrgetter
import time
import matplotlib.pyplot as plt


#---------------------------------------------------------------

"""
Classes/Constructors
"""
class WordEmbeddingBST(object):
    def __init__(self,word,embedding,left=None,right=None):
# word must be a string, embedding can be a list or and array of ints or floats
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)
        self.left = left 
        self.right = right
        
class WordEmbeddingNode(object):
    def __init__(self,word,embedding):
# word must be a string, embedding can be a list or and array of ints or floats
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50)
        
class BTree(object):
    # Constructor
    def __init__(self,data,child=[],isLeaf=True,max_data=5):
        self.data = data
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data
        
#------------------------------------------------------------------

"""
BTree Methods
"""
        
def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    for i in range(len(T.data)):
        if k.word < T.data[i].word:
            return i
    return len(T.data)

def FindChildv2(T,k): #for the search fucntion for nodes
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    for i in range(len(T.data)):
        if k < T.data[i].word:
            return i
    return len(T.data)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.data.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_data//2
    if T.isLeaf:
        leftChild = BTree(T.data[:mid],max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],max_data=T.max_data) 
    else:
        leftChild = BTree(T.data[:mid],T.child[:mid+1],T.isLeaf,max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],T.child[mid+1:],T.isLeaf,max_data=T.max_data) 
    return T.data[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.data.append(i)
    for i in range(len(T.data)):
        for j in range(len(T.data)-1): #sort the nodes in the data list 
            if T.data[j].word > T.data[j+1].word:
                T.data[j],T.data[j+1] = T.data[j+1],T.data[j]

def IsFull(T):
    return len(T.data) >= T.max_data
        
def InsertBTree(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.data =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)
        
def HeightBTree(T):
    if T.isLeaf:
        return 0
    return 1 + HeightBTree(T.child[0])    
    
def PrintBTree(T):
    # Prints data in tree in ascending order
    if T.isLeaf:
        for t in T.data:
            print(t.word,end=' ')
    else:
        for i in range(len(T.data)):
            PrintBTree(T.child[i])
            print(T.data[i].word,end=' ')
        PrintBTree(T.child[len(T.data)])    
 

def SearchBTree(T,k):
    for i in range(len(T.data)): #search through each node of the list data
        if k in T.data[i].word:
            return T.data[i]
    
    if T.isLeaf:
        return None
    
    return SearchBTree(T.child[FindChildv2(T,k)],k)

def NumItemsBTree(T):
    
    num_items = len(T.data)
    
    if not T.isLeaf:
        
        for c in T.child:
            
            num_items += NumItemsBTree(c)
            
    return num_items


def CheckSimilarityBTree(T,first,second):
    dot_product = []
    
    for i in range(len(first)):
        word1 = SearchBTree(T,first[i]) #search for word 1
        word2 = SearchBTree(T,second[i]) #search for word 2
        
        if word1 == None or word2 == None:
            dot_product.append(-1)
        if word1 != None and word2 != None:
            dot_product.append(np.dot(word1.emb,word2.emb) / (np.linalg.norm(word1.emb) *  np.linalg.norm(word2.emb)))
            
    return dot_product 

#-------------------------------------------------------------

"""
Binary Search Tree Methods 
"""

def InsertBST(T,word,embedding):
    if T == None:
        T = WordEmbeddingBST(word,embedding)
    
    elif T.word > word:
        T.left = InsertBST(T.left,word,embedding)
    
    else :
        T.right = InsertBST(T.right,word,embedding)
    
    return T

def HeightBST(T):
    if T == None:
        return 0
    
    leftHeight = HeightBST(T.left)
    rightHeight = HeightBST(T.right)
    
    return 1 + max(leftHeight,rightHeight)
    
def InOrder(T):
    if T is not None:
        InOrder(T.left)
        print(T.word)
        #print(T.emb,'\n')
        InOrder(T.right)
        
def LengthBST(T):
    if T == None:
        return 0
    if T != None:
        return 1 + LengthBST(T.left) + LengthBST(T.right)
    
def SearchForNode(T,k):
    
    if T is None or T.word == k:
        return T
    
    if T.word < k:
        return SearchForNode(T.right,k)
    
    return SearchForNode(T.left,k)


def CheckSimilarityBST(T,first,second):
    dot_product = []
    for i in range(len(first)):
        word1 = SearchForNode(T,first[i]) #search for word 1
        word2 = SearchForNode(T,second[i]) #search for word2
        
        if word1 == None or word2 == None:
            dot_product.append(-1) #shows if one of the words is not in the BST
        if word1 != None and word2 != None:
            dot_product.append(np.dot(word1.emb,word2.emb) / (np.linalg.norm(word1.emb) *  np.linalg.norm(word2.emb)))
            
    return dot_product 

#-----------------------------------------------------------------

"""
Read File Methods
"""      
def ReadFile(file,file_input):
     with open(file,encoding = 'utf8') as f:
        for line in f:
            for item in line.split(): #31875 smaller amount
                if len(file_input) != 31875: 
                    file_input.append(item) 
     return file_input #reads large file

def ReadPairFile(file):
    first = []
    second = []
    pairs = []
    with open(file,encoding = 'utf8') as f:
        for line in f:
            for item in line.split():
                pairs.append(item) #read the pair file
    
    for i in range(0,len(pairs),2):
        first.append(pairs[i])  #first word in pair
        second.append(pairs[i+1]) #second word in pair
         
    return first,second

#-------------------------------------------------------------------
#   Main

if __name__ == "__main__":
    file = 'glove.6B.50d.txt'
    pairs_file = 'pairs.txt'
    T = None

    file_input = []
    first_word = []
    second_word = []
    words = ReadFile(file,file_input)
    first_word,second_word = ReadPairFile(pairs_file)
    print('File Input Length')
    print(len(file_input))
    print('\n')
    
    print('Choose table implementation') #choice from user
    user_choice = int(input('Type 1 for binary search tree or 2 for B-tree: '))
    print('\n')
    
    while user_choice != 1 and user_choice != 2: #in case, 1 or 2 not inputed 
        user_choice = int(input('Please make sure to enter either 1 for binary search tree or 2 for B-tree: '))
        print('\n')

#-----------------------------------------------------------------------
#   BST 

    if user_choice == 1: #BST Option
        print('Binary Search Tree NLP')
        print('---------------------------')
        
        start = time.time() 
        while len(file_input) != 0:
            T = InsertBST(T,file_input[0],file_input[1:51]) #insert BST node
            file_input = file_input[51:]
        end = time.time()
        build_time = end - start #build time
        
        print('Number of Nodes: ',LengthBST(T))
        print('BST height: ', HeightBST(T))
        print('Running time for binary tree construction: ', build_time)
        print('\n')
        
        start1 = time.time()
        cos_sim = CheckSimilarityBST(T,first_word,second_word) #similarity 
        end1 = time.time()
        query_time = end1 - start1
        
        for i in range(len(cos_sim)):
            print('Similarity',first_word[i],',',second_word[i],' = ', cos_sim[i])
        
        print('\n')
        print('Running time for binary search tree query processing: ',query_time) #query time
   
#----------------------------------------------------------------------
#   BTree     

    if user_choice == 2: #BTree Option
        input_max = int(input('Enter maximum number of items stored in each node: '))
        print('\n')
        T = BTree([],max_data = input_max)
        
        print('BTree NLP')
        print('---------------------------')
        
        
        start = time.time()
        while len(file_input) != 0:
            i = WordEmbeddingNode(file_input[0],file_input[1:51]) 
            InsertBTree(T,i) #insert BTree node
            file_input = file_input[51:]
        end = time.time()
        build_time = end - start #build time
        
        print('Number of Nodes: ',NumItemsBTree(T))
        print('BTree height: ', HeightBTree(T))
        print('Running time for BTree construction (with max_items = ',input_max,'): ' , build_time)
        print('\n')
        
        start1 = time.time()
        cos_sim = CheckSimilarityBTree(T,first_word,second_word) #similarity 
        end1 = time.time()
        query_time = end1 - start1 
        
        for i in range(len(cos_sim)):
            print('Similarity',first_word[i],',',second_word[i],' = ', cos_sim[i])
    
        print('\n')
        print('Running time for Btree query processing (with max_items = ',input_max,'): ',query_time) #query time

#----------------------------------------------------------------------

"""
Pair Text Used to Test, Words are within the smaller amount of words used
"""
"""
england europe
germany england
industry information
land japan
leaders japan
england london
december month
policy official
results term
workers family
congress political
home hours
leading league
law lead
small give
nuclear nations
stock dollars
hours workers
workers union
students population
russia russian
march match
of man
see to
see visit
water life
oil million
region oil
london league
"""
    