import numpy as np
import sympy as s
import time

#-------------------------------------------------------------------------

"""
Node Construtor
"""
class WordEmbeddingNode(object):
    def __init__(self,word,embedding):
# word must be a string, embedding can be a list or and array of ints or floats
        self.word = word
        self.emb = np.array(embedding, dtype=np.float32) # For Lab 4, len(embedding=50
        
#----------------------------------------------------------------------------

"""
HashTable Chaining Methods
"""

class HashTableChain(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.bucket = [[] for i in range(size)]

    def insertCH(self,k):
        # Inserts k in appropriate bucket (list) 
        # Does nothing if k is already in the table
        # all six hash functions
#        b = self.h_length_stringCH(k.word)
#        b = self.h_ascii_first_charCH(k.word)
#        b = self.h_ascii_first_last_charCH(k.word)
#        b = self.h_sum_asciiCH(k.word)
        b = self.h_recursiveCH(k.word)
#        b = self.h_ascii_plus_length(k.word)
        if not k in self.bucket[b]:
            self.bucket[b].append(k) #Insert new item at the end
            
    def findCH(self,k):
        # Returns bucket (b) and index (i) 
        # If k is not in table, a == -1
        # all six hash functions
#        b = self.h_length_stringCH(k)
#        b = self.h_ascii_first_charCH(k)
#        b = self.h_ascii_first_last_charCH(k)
#        b = self.h_sum_asciiCH(k)
        b = self.h_recursiveCH(k)
#        b = self.h_ascii_plus_length(k)
        try:
            for i in range(len(self.bucket)):
                if k == self.bucket[b][i].word: #compares word to word within a list in the bucket
                    a = self.bucket[b][i]
                    return b,a #returns the hash and the node
        except:
            a = -1
        return b, a
     
    def print_tableCH(self):
        print('Table contents:')
        for b in self.bucket:
            print(b)
    
    
    def h_length_stringCH(self,k):
        size = len(k)
        return size%len(self.bucket)
    
    def h_ascii_first_charCH(self,k):
        a_value = 0
        if k != None:
            a_value = ord(k[0])
            
        return a_value %len(self.bucket)
    
    def h_ascii_first_last_charCH(self,k):
        if len(k) != None:
            first_value = ord(k[0])
            last_value = ord(k[-1])
            product = first_value * last_value
            
        return product%len(self.bucket)
    
    def h_sum_asciiCH(self,k):
        sum_ascii = 0
        if k != None:
            for i in range(len(k)):
                sum_ascii += ord(k[i])
                
        return sum_ascii %len(self.bucket)
    
    def h_recursiveCH(self,k):
        if k == None:
            return 1%len(self.bucket)
        if len(k) == 1:
            return ord(k[0])%len(self.bucket)
        else :  
            return (ord(k[0])+255*self.h_recursiveCH(k[1:]))%len(self.bucket)
    
    def h_ascii_plus_length(self,k):
        sum_ascii_length = 0
        if k != None:
            for i in range(len(k)):
                sum_ascii_length += ord(k[i])
        
        sum_ascii_length += len(k)
        
        return sum_ascii_length%len(self.bucket)
    
    def CheckSimilarityHChain(self,first,second):
        dot_product = []
        
        for i in range(len(first)):
            a,word1 = self.findCH(first[i]) #search for word 1
            b,word2 = self.findCH(second[i]) #search for word 2

            
            if word1 == None or word2 == None:
                dot_product.append(-1)
            if word1 != None and word2 != None:
                dot_product.append(np.dot(word1.emb,word2.emb) / (np.linalg.norm(word1.emb) *  np.linalg.norm(word2.emb)))
            
        return dot_product 
    
#----------------------------------------------------------------

"""
HashTable Linear Probing Methods
"""
        
class HashTableLP(object):
    # Builds a hash table of size 'size', initilizes items to -1 (which means empty)
    # Constructor
    def __init__(self,size):  
        self.item = np.zeros(size,dtype=object)-1 #dtype object so that it will fill with -1 but still take nodes
 
    def insertLP(self,k):
        # Inserts k in table unless table is full
        # Returns the position of k in self, or -1 if k could not be inserted
        # all six hash functions
        for i in range(len(self.item)): #Despite for loop, running time should be constant for table with low load factor
            pos = self.h_length_stringCH(k.word,i)
#            pos = self.h_ascii_first_charCH(k.word,i)
#            pos = self.h_ascii_first_last_charCH(k.word,i)
#            pos = self.h_sum_asciiCH(k.word,i)
#            pos = self.h_recursiveCH(k.word,i)
#            pos = self.h_ascii_plus_length(k.word,i)
            
            if self.item[pos] == -1: #if the spot is empty then it inserts
                self.item[pos] = k
                return pos
        return -1
    
    def findLP(self,k):
        # Returns the position of k in table, or -1 if k is not in the table
        # all six hash functions
        for i in range(len(self.item)):
            pos = self.h_length_stringCH(k,i)
#            pos = self.h_ascii_first_charCH(k,i)
#            pos = self.h_ascii_first_last_charCH(k,i)
#            pos = self.h_sum_asciiCH(k,i)
#            pos = self.h_recursiveCH(k,i)
#            pos = self.h_ascii_plus_length(k,i)
            if self.item[pos] == -1:
                return -1
            if self.item[pos].word == k: #if word in node in the item list is equal to k
                return self.item[pos]       
        return -1         
    
    def print_tableLP(self):
        print('Table contents:')
        print(self.item)
        
    def h_length_stringCH(self,k,a):
        size = len(k) + a
        return size%len(self.item)
    
    def h_ascii_first_charCH(self,k,a):
        a_value = 0
        if k != None:
            a_value = ord(k[0]) + a
            
        return a_value %len(self.item)
    
    def h_ascii_first_last_charCH(self,k,a):
        if len(k) != None:
            first_value = ord(k[0])
            last_value = ord(k[-1])
            product = first_value * last_value
            product += a
            
        return product%len(self.item)
    
    def h_sum_asciiCH(self,k,a):
        sum_ascii = 0
        if k != None:
            for i in range(len(k)):
                sum_ascii += ord(k[i])
                sum_ascii += a
                
        return sum_ascii %len(self.item)
    
    def h_recursiveCH(self,k,a):
        if k == None:
            a = 1%len(self.item) + a
            return a
        if len(k) == 1:
            b = ord(k[0])%len(self.item) + a
            return b
        else :  
            return (ord(k[0])+255*self.h_recursiveCH(k[1:],a))%len(self.item)
    
    def h_ascii_plus_length(self,k,a):
        sum_ascii_length = 0
        if k != None:
            for i in range(len(k)):
                sum_ascii_length += ord(k[i])
        
        sum_ascii_length += len(k)
        sum_ascii_length += a
        
        return sum_ascii_length%len(self.item)
    
    
    def CheckSimilarityHLP(self,first,second):
        dot_product = []
        
        for i in range(len(first)):
            word1 = self.findLP(first[i]) #search for word 1
            word2 = self.findLP(second[i]) #search for word 2

            
            if word1 == None or word2 == None:
                dot_product.append(-1)
            if word1 != None and word2 != None:
                dot_product.append(np.dot(word1.emb,word2.emb) / (np.linalg.norm(word1.emb) *  np.linalg.norm(word2.emb)))
            
        return dot_product 


#------------------------------------------------------------------

"""
Read File Methods
"""      
def ReadFile(file,file_input):
     with open(file,encoding = 'utf8') as f:
        for line in f:
            for item in line.split(): #31875 smaller amount
                if len(file_input) != 31875: #637500
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

"""
Main
"""
#------------------------------------------------------------------

if __name__ == "__main__":
    file = 'glove.6B.50d.txt'
    pairs_file = 'pairs.txt'

    file_input = []
    first_word = []
    second_word = []
    words = ReadFile(file,file_input)
    first_word,second_word = ReadPairFile(pairs_file)
    print('File Input Length')
    print(len(file_input))
    print('\n')
    size =  s.nextprime(len(words)/51)
    
    print('Choose table implementation') #choice from user
    user_choice = int(input('Type 1 for HashTable Chaining or 2 for HashTable Linear Probing: '))
    print('\n')
    
    while user_choice != 1 and user_choice != 2: #in case, 1 or 2 not inputed 
        user_choice = int(input('Please make sure to enter either 1 for HashTable Chaining or 2 for HashTable Linear Probing: '))
        print('\n')
    
#-------------------------------------------------------------------

    if user_choice == 1:
        h = HashTableChain(size)
        
        start = time.time()
        while len(file_input) != 0:
            i = WordEmbeddingNode(file_input[0],file_input[1:51])
            h.insertCH(i)
            file_input = file_input[51:]
        end = time.time()
        build_time = end - start
        
        print('Running time for HashTable Chaining construction: ', build_time)
        print('\n')
        
        start1 = time.time()
        cos_sim = h.CheckSimilarityHChain(first_word,second_word) #similarity
        end1 = time.time()
        query_time = end1 - start1
        
        for i in range(len(cos_sim)):
            print('Similarity',first_word[i],',',second_word[i],' = ', cos_sim[i])
        
        print('\n')
        print('Running time for HashTable Chaining query processing: ',query_time) #query time
    
#---------------------------------------------------------------------

    if user_choice == 2:
        H = HashTableLP(size)
        
        start = time.time()
        while len(file_input) != 0:
            i = WordEmbeddingNode(file_input[0],file_input[1:51])
            H.insertLP(i)
            file_input = file_input[51:]
        end = time.time()
        build_time = end - start
        
        print('Running time for HashTable Linear Probing construction: ', build_time)
        print('\n')
        
        start1 = time.time()
        cos_sim = H.CheckSimilarityHLP(first_word,second_word) #similarity
        end1 = time.time()
        query_time = end1 - start1
        
        for i in range(len(cos_sim)):
            print('Similarity',first_word[i],',',second_word[i],' = ', cos_sim[i])
            
        print('\n')
        print('Running time for HashTable Linear Probing query processing: ',query_time) #query time
        
        
    
    