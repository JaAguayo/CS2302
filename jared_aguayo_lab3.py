#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:04:35 2019

@author: jaredaguayo
"""
"""
class: CS 2302
author: Jared Aguayo
Assignment: Lab 3
Instrcutor: Olac Fuentes
T.A.: Anindita Nath
October 6 2019 - last modified
Purpose: Implement the class SortedList that is identical to the List class described in class, except that its elements
are sorted in ascending order at all times and implement functions for this class and compare the running time
of sorted list functions and non sorted list functions 
"""
import math

class Node(object):
    # Constructor
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next
"""
#########################################
Sorted List
#########################################
"""

    
class SortedList(object):   
    # Constructor
    def __init__(self,head = None,tail = None):    
        self.head = head
        self.tail = tail
   
    def Print(self):
        t = self.head
        while t is not None:
            print(t.data,end=' ')
            t = t.next
        print()
        
    def GetLength(self):
        count = 0
        t = self.head 
        while t is not None:
          count += 1
          t = t.next
        return count 
            
    def Append(self,x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
            
    def AppendList(self,python_list):
        for d in python_list:
            self.Append(d)
    
    def Insert(self,i):
        t = self.head
        
        if self.head == None: #if the list is empty it sets the node to head and tail
            self.head = i
            self.tail = self.head
            return t
        
        while t is not None and t.next.data < i.data:
            t = t.next #loops until it finds data that is larger then insert node data
                
        i.next = t.next #input the node passed in
        t.next = i  
        
        return t

    def Delete(self,i):
        t = self.head
        while t is not None:
            if t.next != None and t.next.data == i: #if the data of the next node in the list matches the 
                t.next = t.next.next # passed in data then it sets that nodes next pointer to the node after next
                return t
            t = t.next
        return t
    
    def Merge(self,M):
        t = self.head
        i = M.head
        
        while i is not None: #this outer loop will go until M list reaches None
            while t is not None and t.next.data < i.data: #loops through list for each Node of M
                t = t.next # loops until it finds data that is larger then the node data of M list
            
            temp = i.data #temp to hold value of the M node
            n = Node(temp) #makes a node to insert into the t list
            n.next = t.next #inputs the new node into t list
            t.next = n
            
            i = i.next
            
        return t
    
    def IndexOf(self,i):
        t = self.head
        index = 0 #counts how many nodes it passes 
        
        if self.head == None: 
            return -1
        
        while t is not None:
            if t.data == i: #if the data in the node for t is the same as i
                return index #return the counter
            else:
                t = t.next
                
            index += 1 #increment indexer
            
        return -1 #if it goes through without fidning i in list it returns -1
    
    def Clear(self):
        t = self.head
        while t is not None:
            last = t.next #gets node from the next
            del t.data #deletes current node data
            t = last #sets that now deleted node position to last or what used to be next
    
    def Min(self):
        if self.head == None:
            return math.inf
        
        return self.head.data #returns head because sorted list,smallest at the beginning
    
    def Max(self):
        if self.head == None:
            return math.inf
        
        return self.tail.data #returns tail because the largest node is at the end
    
    def HasDuplicates(self):
        
        if self.head == None or self.head.next == None: #if the list is less then 2 nodes its false
            return False
        
        t = self.head
        while t is not None:
            if t.next != None:
                if t.data == t.next.data: #since sorted you can just check next to see if its the same
                    return True
            t = t.next
        
        return False
    
    def Select(self,k):
        if self.head == None:
            return math.inf
        
        length = self.GetLength() #gets length to check if k is even within bounds
        
        if length < k: #check if k is in bounds
            return math.inf
        
        t = self.head
        index = 0 #index counter
        
        while t is not None:
            if index == k: #if the index counter equals k then it returns the data
                return t.data 
            index += 1
            t = t.next
"""
##########################################
Non-Sorted List for Comparison
##########################################
"""
          
class List(object):   
    # Constructor
    def __init__(self,head = None,tail = None):    
        self.head = head
        self.tail = tail
    
    def Print(self):
        t = self.head
        while t is not None:
            print(t.data,end=' ')
            t = t.next
        print()
        
    def GetLength(self):
        count = 0
        t = self.head 
        while t is not None:
          count += 1
          t = t.next
        return count 
            
    def Append(self,x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
            
    def AppendList(self,python_list):
        for d in python_list:
            self.Append(d)
    
    def Insert(self,i):
        if self.head == None:
            self.head = i
            self.tail = self.head
            
        self.tail.next = i #inserts at the end
        self.tail = self.tail.next
    
    def Delete(self,i):
        t = self.head
        while t is not None:
            if t.next != None and t.next.data == i:
                t.next = t.next.next
                return t
            t = t.next
        return t
    
    def Merge(self,M):
        i = M.head
        while i is not None:
             self.tail.next = i #inserts each node of M at the end
             self.tail = self.tail.next
             i = i.next
    
    def IndexOf(self,i):
        t = self.head
        index = 0
        
        if self.head == None:
            return -1
        
        while t is not None:
            if t.data == i:
                return index
            else:
                t = t.next
                
            index += 1
            
        return -1
    
    def Clear(self):
        t = self.head
        while t is not None:
            last = t.next
            del t.data
            t = last
    
    def Min(self):
        if self.head == None:
            return math.inf
        
        smallest = self.head.data #set samllest to head
        t = self.head
        
        while t is not None:
            if t.data < smallest: 
                smallest = t.data #updates smallest everytime a smaller number appears
                
            t = t.next
        return smallest 
    
    def Max(self):
        if self.head == None:
            return math.inf
        
        biggest = self.head.data #set biggest to head
        t = self.head
        
        while t is not None:
            if t.data > biggest: 
                biggest = t.data #updates biggest everytime a bigger number appears
                
            t = t.next
        return biggest
    
    def HasDuplicates(self):
        
        if self.head == None or self.head.next == None:
            return False
        
        t = self.head
        while t is not None:
            if t.next != None:
                if t.data == t.next.data:
                    return True
            t = t.next
        
        return False
    
    def Select(self,k):
        if self.head == None:
            return math.inf
        
        length = self.GetLength()
        
        if length < k:
            return math.inf
        
        t = self.head
        index = 0
        
        while t is not None:
            if index == k:
                return t.data 
            index += 1
            t = t.next
"""
#############################################
Main
#############################################
"""

if __name__ == "__main__":
    L4 = SortedList()
    L1 = SortedList()
    L2 = SortedList()
    L3 = List()
    L5 = List()
    
    L4.AppendList(sorted([9,2,45,4,5,24,8,33])) #sends sorted lists
    L1.AppendList(sorted([2,1,5,6,9,10,21,23,23,45]))
    print('Sorted Lists', '\n')
    print('Starting List')
    print('------------------')
    L1.Print()
    print('\n')
    print('Insert Node 7')
    print('------------------')
    i = Node(7)
    L1.Insert(i)
    L1.Print()
    print('\n')
    print('Delete Node 9')
    print('------------------')
    L1.Delete(9)
    L1.Print()
    print('\n')
    print('Delete Node 11')
    print('------------------')
    L1.Delete(11)
    L1.Print()
    print('\n')
    x = L1.IndexOf(6)
    print('Index of Number')
    print('------------------')
    print(x)
    print('\n')
    x = L1.Min()
    print('Min')
    print('------------------')
    print(x)
    print('\n')
    x = L1.Max()
    print('Max')
    print('------------------')
    print(x)
    print('\n')
    x = L1.HasDuplicates()
    print('Duplicates')
    print('------------------')
    print(x)
    print('\n')
    x = L1.Select(6)
    print('Number at index k')
    print('------------------')
    print(x)
    print('\n')
    print('Merge 2 Sorted Lists')
    print('------------------')
    L1.Merge(L4)
    L1.Print()
    print('\n')
    L1.Clear()
    
    
    L2.AppendList([])
    print('Min of Empty List')
    print('------------------')
    x = L2.Min()
    print(x)
    print('\n')
    print('Duplicates of Empty List')
    print('------------------')
    x = L2.HasDuplicates()
    print(x)
    print('\n')
    print('Index of Empty List')
    print('------------------')
    x = L2.IndexOf(3)
    print(x)
    print('\n')
    print('Insert into an Empty List')
    print('------------------')
    i = Node(7)
    L2.Insert(i)
    L2.Print()
    print('\n')
    print('\n')
    
    print('Non Sorted Lists Outputs of Code that differs from Sorted','\n')
    L5.AppendList([33,43,12,1,3,4,5])
    L3.AppendList([12,43,78,5,2,14,1,6])
    print('Starting List')
    print('------------------')
    L3.Print()
    print('\n')
    print('Insert Node')
    print('------------------')
    i = Node(7)
    L3.Insert(i)
    L3.Print()
    print('\n')
    print('Find Min')
    print('------------------')
    x = L3.Min()
    print(x)
    print('\n')
    print('Find Max')
    print('------------------')
    x = L3.Max()
    print(x)
    print('\n')
    print('Merge 2 Lists')
    print('------------------')
    L3.Merge(L5)
    L3.Print()
    print('\n')
