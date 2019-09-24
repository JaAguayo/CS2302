#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:25:24 2019

@author: jaredaguayo
"""
"""
class: CS 2302
author: Jared Aguayo
Assignment: Lab 2
Instrcutor: Olac Fuentes
T.A.: Anindita Nath
23 September 2019 - last modified
Purpose:Make sorting methods, bubble and quicksort,that looks for the smallest 
element.Then use knowledge of activiation records to modify quicksort 
method, and then find the big O notation of the methods created
"""
"""
Part 1 
"""
"""
Reset List 
"""
def reset_list(L_copy): #to reset the list so each method can sort
    L = L_copy[:]
    return L
"""
Bubble Sort 
"""
def select_bubble(L,K):
    if_elements_switch = 0 #check if any switches happen
    
    for i in range(0,len(L)-1):
        if L[i] > L[i+1]:
            L[i],L[i+1] = L[i+1],L[i] #switch elements
            if_elements_switch += 1
            
    if if_elements_switch == 0: #if there are no switches then the 
       return L                 #list is returned since its sorted
    else:
        select_bubble(L,K) #recusive call if the list isnt sorted
    
    return L[K]
"""
Quicksort 
"""
def select_quick(L,K,first,last):
    if first < last:
        
        p = partition(L,first,last) #returns index of p
        
        select_quick(L,K,first, p-1) #sorts elements less then pivot index
        select_quick(L,K,p +1, last) #sorts elements more then pivot index
        
    return L[K] 

"""
Partisian
"""
def partition(L,first,last):
    
    pivot = L[first] #first element as index

    left_side = first+1 #left starts 1 past 1st index
    right_side = last #starts last element
    stop = False #boolean to stop while loop
   
    while not stop:

       while left_side <= right_side and L[left_side] <= pivot: #checks if left is less or eqaul to right 
           left_side += 1   #as well as less then pivot, then add to left

       while L[right_side] >= pivot and right_side >= left_side: #checks if right is greater then or equal
           right_side -= 1  #to left side as well as greater then or equal to pivot, then subtract from right

       if right_side < left_side: #if right is less then left it will break the loop
          stop = True
          
       else: 
           L[left_side],L[right_side] = L[right_side],L[left_side] #when both of the while loops reach 
           #an element that broke the loop then they have to be swapped
   
    L[first],L[right_side] = L[right_side],L[first] #puts pivot in place

    return right_side #returns pivots index

"""
Modified Quicksort
"""
def select_modified_quick(L,K,first,last):
    if first < last:
        p = partition(L,first,last)
        
        if K == p: #if k is the index of the p
            
            return L[K]
        
        elif K < p: #if K is on left side of p
            
            select_modified_quick(L,K,first, p-1)
            
        elif K > p: #if K is on right side of p
        
            select_modified_quick(L,K,p+1 , last)
            
    return L[K]
"""
Part 2 
"""
"""
Quicksort using stacks
"""
class stackRecord(object):
      # Constructor
    def __init__(self, L, K, first, last):  
        self.L = L
        self.K = K
        self.first = first
        self.last = last

def stack_quick(L,K,first,last):
    stack = [stackRecord(L,K,first,last)]
    while len(stack)>0: #if the length of stack is 0 it breaks
        if first < last: #first has to be less then last
            q = stack.pop(-1) #pop which will eveuntually break the loop
            
            p = partition(q.L,q.first,q.last)
            
            if q.K > p: #push on to stack if K index is greater then p
                stack.append(stackRecord(q.L,q.K,p+1, q.last))
                
            elif q.K < p: #push on to stack if K index is less then the p
                stack.append(stackRecord(q.L,q.K,q.first,p-1))
            else :
                return L[K]
"""
while loop sort
"""
def select_while_quick(L,K,first,last):
    p = partition(L,first,last)
    
    while p != K:
        
        if K < p: #if K less then p index partition left side
            p = partition(L,first,p-1)
        else: #else just partition the right side
            p = partition(L,p+1,last)
    
    return L[K]
"""
Main
"""
    
K = 4
L = [23,33,20,48,50,-45,89,54,0,67,99,22,100,3]
L_copy= [23,33,20,48,50,-45,89,54,0,67,99,22,100,3] #copy to reset list each sort

print('The Kth element in the sorted list:','\n')

print('Bubble Sort')
print(select_bubble(L,K))
L = reset_list(L_copy)

print('Quick Sort')
print(select_quick(L,K,0,len(L)-1))
L = reset_list(L_copy)

print('Quick Sort, One Recursive Call')
print(select_modified_quick(L,K,0,len(L)-1))
L = reset_list(L_copy)

print('Quick Sort with While Loop')
print(select_while_quick(L,K,0,len(L)-1))
L = reset_list(L_copy)

print('Quick Sort using Stacks')
print(stack_quick(L,K,0,len(L)-1))
L = reset_list(L_copy)
