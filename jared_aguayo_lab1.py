#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
class: CS 2302
author: Jared Aguayo
Assignment: Lab 1
Instrcutor: Olac Fuentes
T.A.: Anindita Nath
8 September 2019 - last modified
Purpose: This program uses an input word from the user
and finds anagrams amongst a large data set of words
"""
import time #to get the time of the program

"""
FIND_ANAGRAMS
The find_anagram method finds anagrams checking if permutations in a list are in
a set of words
"""
#----------------------------------------------------------------
def find_anagrams(set_words,anagrams,permutations):
    
    if len(permutations) == 0: #Base case 1: when permutation list has length 0
        return anagrams
    
    else :
        if permutations[0] in set_words: #checks if a permutation is in the set of words
            anagrams.add(permutations[0]) #if its in the set it will add it to an anagram set
            return find_anagrams(set_words,anagrams,permutations[1:])
            #recursive calls will shorten the list each call
        else: 
            return find_anagrams(set_words,anagrams,permutations[1:])
    
#----------------------------------------------------------------------
"""
FIND_PERMUTATIONS
The find_permutations method finds all the permutations of the word inputed
and has no duplicates 
"""
def find_permutations(remain_letters, scram_letters,permutations):
    
    if len(remain_letters) == 0:
        # Base case: All letters used
        permutations.add(scram_letters)

    else:
        # move a letter from remaining to scrambled
        for i in range(len(remain_letters)):
            # The letter at index i will be scrambled
            scramble_letter = remain_letters[i]
            
            # Remove letter to scramble from remaining letters list
            remaining_letters = remain_letters[:i] + remain_letters[i+1:]
            # Scramble letter
            find_permutations(remaining_letters, scram_letters + scramble_letter,permutations)
            
    return permutations
#------------------------------------------------------------------------
    
#MAIN
#------------------------------------------------------------------------
print('The Anagram Program')
print('-------------------')
    
set_words =  set(open('words_alpha.txt').read().split()) #gets set of words from file
#set_words = set() #------- TEST CODE TO CHECK IF TEXT IS EMPTY 

#Check if text file is empty, if it is the program will end
#----------------------------------------------------------------------
if len(set_words) == 0: #
    print('The list of words provided is empty!')
    word_inputted = '' #if the text file is empty it will end the program
else :
    word_inputted = 'hh' #just gave it a random value to start the while loop
#----------------------------------------------------------------------

while word_inputted != '': #while loop to continue asking for string until an empty string is given
    
    permutations = set()
    anagrams = set() 
    
    word_inputted = input('Enter a word or an empty string to exit: ')
    
 #Check if the user inputs a digit, it will continue asking until a string is inputed   
#------------------------------------------------------------------------
    is_input_digit = word_inputted.lstrip('-').isdigit() #true if a digit,false if not
                                                         #lstrip - removes a negative from front 
                                                         
    while is_input_digit == True : #while loop to make sure input is a string 
        word_inputted = input('Please input either a word or an empty string to exit: ')
        is_input_digit = word_inputted.isdigit() #if its a digit is makes the user re input
#-------------------------------------------------------------------------
        
    word_inputted = word_inputted.lower() #if any capital letters are inputted, change to lowercase

    if word_inputted == '' : #exit function
        print('Thanks for using the anagram program!')
        
    else :
        start = time.time() #gives the time that it takes for the method to run
        permutations = (find_permutations(word_inputted,'',permutations)) #gets permutations
        list_permutations = list(permutations) #cast from set to list so there is no duplicates
        list_permutations.remove(word_inputted) #remove the word inputed as a permutation
        anagrams = ((find_anagrams(set_words,anagrams,list_permutations))) #gets anagrams
        end = time.time()
        #Print outs
        print('The word', word_inputted,'has', len(anagrams), 'anagrams:', end = '\n\n')
        
        for i in sorted(anagrams): #print set alphabetical
            print(i)
        
        print('\n','It took', end - start, 'seconds to find the anagrams.')
        
        
        
        
            
        
"""
VARIABLES FOR OTHER FUNCTIONS
-------------------------------
list_words = list(set_words) #changed into a list
words = sorted(list_words, key=len) #sorted based on length of the strings in list,ascending
empty list to store the anagrams that the method finds
permutations = set()
"""
        

"""
OTHER FUNCTIONS TO FIND ANAGRAMS
--------------------------------------
  if len(words) == 0: 
        return anagrams
    
    if len(words[0]) > len(word_inputed):
        return anagrams

    elif len(word_inputed) != len(words[0]):
        return find_anagrams(word_inputed,words[1:],anagrams)
    
    else :
        if sorted(word_inputed) == sorted(words[0]):
            anagrams.append(words[0])
            return find_anagrams(word_inputed, words[1:],anagrams)
        
        else :
            return find_anagrams(word_inputed,words[1:],anagrams)
    
"""

"""
def find_anagrams(word_inputed,words,anagrams):
    if len(words) == 0: 
        return anagrams
    
    for i in range(len(words)):
    
        if len(words[i]) > len(word_inputed):
            return anagrams
    
        elif len(word_inputed) != len(words[i]):
            continue
        
        else :
            if sorted(word_inputed) == sorted(words[i]):
                anagrams.append(words[i])
                return find_anagrams(word_inputed, words[i+1:],anagrams)
"""
"""
def find_anagrams(set_words,anagrams,permutations):
    
    if len(permutations) == 0:
        return anagrams
    
    else : 
        if permutations[0] in set_words:
            anagrams.add(permutations[0])
            return find_anagrams(set_words,anagrams,permutations[1:])
        
        else: 
            return find_anagrams(set_words,anagrams,permutations[1:])
"""
"""
def find_anagrams(set_words,anagrams,permutations):
    
    anagrams = permutations.intersection(set_words) #gives anagrams using intersection
    
    return anagrams
"""
