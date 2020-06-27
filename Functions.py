"""
Purpose : Functions needed to complete a game of Yahtzee 
    
Created on 17/6/2020
@author: Murray Keogh

Program description: 
    Functions needed to complete a game of Yahtzee.  Further description
    of each function within the function notes. 
   
Function dictionary:
    
   roll_die          : Rolls the selected die.
   choice            : Decides which die to roll again.
   final_die         : Which score to update based on final die. 
   
   
"""

import numpy as np
import random as rand
import pandas as pd


die_array = np.zeros(6,dtype=int)

def roll_dice(die_array):
    
    """
    Purpose : Accepts array of six die results. Only rolls for zero. 

    Data dictionary:
    
        die_array         : Array of six die results.
   
    """
    for k in range(0,len(die_array)):
      
        if die_array[k] == 0:
            die_array[k] = rand.randint(1,6)
    return die_array
        
    
    
    
def choice(die_array,score_check):
    

    """
    Purpose : Accepts array of six die results. Choose which to result to keep
    and which to roll again (set to zero). 

    Data dictionary:
        die_array         : Array of six die results.
        lrg_straight_one  : Array, first option die needed to make large str.
        lrg_straight_two  : Array, second option die needed to make large str.
        smol_str_one      : Array, first option die needed to make smol str. 
        smol_str_two:     : Array, second option die needed to make smol str.
        smol_str_three    : Array, third option die needed to make smol str.
        unique_val        : Series, unique value count of results
    """
    
    #Initialize variables
    
    #create numpy array of die_array
    #np_die_array = np.array(die_array)
    
    #Choice variable
    
    choice = 999
    
    #Check for large vs small straight
    ls_check = True 
    x_kind_check = True
    fh_check = True

    
    #Options for large and small straights
    lrg_str_one = [1,2,3,4,5]
    lrg_str_two = [2,3,4,5,6]
    smol_str_one = [1,2,3,4]
    smol_str_two = [2,3,4,5]
    smol_str_three = [3,4,5,6]
    
    #Create series of unique value counts
    unique_val = pd.value_counts(die_array)
    
    #Get counts of each die face
   #num_one = np.count_nonzero(np_die_array == 1)
   #num_two = np.count_nonzero(np_die_array == 2)
   #num_three = np.count_nonzero(np_die_array == 3)
   #num_four = np.count_nonzero(np_die_array == 4)
   #num_five = np.count_nonzero(np_die_array == 5)
   #num_six = np.count_nonzero(np_die_array == 6)
    
    #Yahtzee
    
    if len(set(die_array)) == 1:
        #print("Yahtzee!")
        choice = 11
        die_array = die_array
        
    
    #Large Straight
    
    if ((all(z in die_array for z in lrg_str_one)) \
    or (all(z in die_array for z in lrg_str_two))) \
    and score_check[9] \
    and choice == 999:
        #print("Large Straight!")
        ls_check = False
        choice = 9
        die_array = die_array
        
        
    #Small Straight
    
    if ((all(z in die_array for z in smol_str_one)) \
    or (all(z in die_array for z in smol_str_two)) \
    or (all(z in die_array for z in smol_str_three))) \
    and ls_check \
    and score_check[8] \
    and choice == 999:
        #print("Smol Straight!")
        choice = 8
        die_array = die_array
        #further work : change last die to go for large straight
        
    #Full House
    
    if len(set(die_array)) == 2 \
    and unique_val.iloc[0]==3 \
    and unique_val.iloc[1]==2 \
    and score_check[10]\
    and choice == 999:
        #print("Full House!")
        choice = 10
        fh_check = False
        die_array = die_array
        
    
    
    #Four of a Kind
    
    if unique_val.iloc[0] == 4 \
    and score_check[7] \
    and choice == 999:
        #print("Four of a kind")
        face = unique_val.index[0]
        x_kind_check = False
        choice = 7
        for k in range(0,len(die_array)):
            if die_array[k] == face:
                die_array[k] = die_array[k]
            else:
                die_array[k] = 0
        
    #Three of a Kind
    
    if unique_val.iloc[0] == 3 \
    and x_kind_check \
    and fh_check \
    and score_check[6] \
    and choice == 999:
        #print("Three of a kind")
        face = unique_val.index[0]
        x_kind_check = False
        choice = 6
        
        for k in range(0,len(die_array)):
            if die_array[k] == face:
                die_array[k] = die_array[k]
            else:
                die_array[k] = 0
    #Six
    if unique_val.iloc[0] >= 2 \
    and x_kind_check \
    and fh_check \
    and unique_val.index[0] ==6 \
    and score_check[5] \
    and choice == 999:
        #print(6)
        choice = 5
        for k in range(0,len(die_array)):
            if die_array[k] == 6:
                die_array[k] = die_array[k]
            else:
                die_array[k] = 0
                
    #Five
    if unique_val.iloc[0] >= 2 \
    and x_kind_check \
    and fh_check\
    and unique_val.index[0] == 5 \
    and score_check[4] \
    and choice == 999:
        #print(5)
        choice = 4
        for k in range(0,len(die_array)):
            if die_array[k] == 5:
                die_array[k] = die_array[k]
            else:
                die_array[k] = 0
                
                
    #Four
    if unique_val.iloc[0] >= 2 \
    and x_kind_check \
    and fh_check \
    and unique_val.index[0] ==4 \
    and score_check[3] \
    and choice == 999:
        #print(4)
        choice = 3
        for k in range(0,len(die_array)):
            if die_array[k] == 4:
                die_array[k] = die_array[k]
            else:
                die_array[k] = 0
                

    #Three
    if unique_val.iloc[0] >= 2 \
    and x_kind_check \
    and fh_check \
    and unique_val.index[0] == 3 \
    and score_check[2] \
    and choice == 999:
        #print(3)
        choice = 2
        for k in range(0,len(die_array)):
            if die_array[k] == 3 :
                die_array[k] = die_array[k]
            else:
                die_array[k] = 0
                
    #Two
    if unique_val.iloc[0] >= 2 \
    and x_kind_check \
    and fh_check \
    and unique_val.index[0] == 2 \
    and score_check[1] \
    and choice == 999:
        #print(2)
        choice = 1
        for k in range(0,len(die_array)):
            if die_array[k] == 2 :
                die_array[k] = die_array[k]
            else:
                die_array[k] = 0
                
    #One
    if unique_val.iloc[0] >= 2 \
    and x_kind_check \
    and fh_check \
    and unique_val.index[0] == 1 \
    and score_check[0] \
    and choice == 999:
        #print(1)
        choice = 0
        for k in range(0,len(die_array)):
            if die_array[k] == 1 :
                die_array[k] = die_array[k]
            else:
                die_array[k] = 0
    
    #Chance
    if choice == 999 \
    and score_check[12]:
        #print("Chance")
        choice = 12
        for k in range(0,len(die_array)):
            if die_array[k] >= 3 :
                die_array[k] = die_array[k]
            else:
                die_array[k] = 0
                
    #Roll All Again
    if choice == 999:
        #print("Chance")
        for k in range(0,len(die_array)):
                die_array[k] = 0
      
    
    return(die_array,choice)
    
def round_score(die_array,score_check,score_array,choice):
    

    """
    Purpose : Accepts array of six die results. Depending on values, updates the score
    array with score for round. 

    Data dictionary:
        die_array         : Array of six die results.
        score_check       : Boolean Array, true if no score, false if score.
        score_array       : Array, score for each category.
    
    """

    
    #Chance score
    if choice == 12:
        score_array[12] = np.sum(die_array)
        score_check[12] = False
        
    #Yahtzee score
    if choice == 11:
        score_array[11] = 50
        score_check[11] = False
        
    #Full House score
    if choice == 10:
        score_array[10] = 25
        score_check[10] = False
        
    #Large Straight score
    if choice == 9:
        score_array[9] = 40
        score_check[9] = False
        
    #Small Straight score
    if choice == 8:
        score_array[8] = 30
        score_check[8] = False
        
    #Four of a Kind score
    if choice == 7:
        score_array[7] = np.sum(die_array)
        score_check[7] = False
        
    #Three of a Kind score
    if choice == 6:
        score_array[6] = np.sum(die_array)
        score_check[6] = False
        
    #Six score
    if choice == 5:
        score = 0
        for k in range(0,len(die_array)):
            if die_array[k] == 6 :
                score = score+6

        score_array[5] = score
        score_check[5] = False
        
    #Five score
    if choice == 4:
        score = 0
        for k in range(0,len(die_array)):
            if die_array[k] == 5 :
                score = score+5

        score_array[4] = score
        score_check[4] = False
        
    #Four score
    if choice == 3:
       score = 0
       for k in range(0,len(die_array)):
            if die_array[k] == 4 :
                score = score+4

       score_array[3] = score
       score_check[3] = False
        
    #Three score
    if choice == 2:
        score = 0
        for k in range(0,len(die_array)):
            if die_array[k] == 3 :
                score = score+3

        score_array[2] = score
        score_check[2] = False
        
    #Two score
    if choice == 1:
        score = 0
        for k in range(0,len(die_array)):
            if die_array[k] == 2 :
                score = score+2

        score_array[1] = score
        score_check[1] = False
        
    #One score
    if choice == 0:
        score = 0
        for k in range(0,len(die_array)):
            if die_array[k] == 1 :
                score = score+1

        score_array[0] = score
        score_check[0] = False
        

    return score_array,score_check
    
        
        
        



















