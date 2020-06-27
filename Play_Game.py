"""
Purpose : Plays one full game of Yahtzee
    
Created on 17/6/2020
@author: Murray Keogh

Program description: 
    Using functions, complete one full game of Yahtzee. 
   
Function dictionary:
    
   play_game         : Function to play a game of Yahtzee 
   
"""

#Initialize 
import numpy as np
import Functions as fun

def play_game():
    
    """
    Purpose : Function to play a game of Yahtzee

    Data dictionary:
        score_check        : Array, hold which cats have been scored
        score_array        : Array, score for each category.
        die_array          : Array, holds the current die roll and used to roll next round
        choices            : tuple, holds die_array and choice
        final_choice       : int, holds the final choice used for scoring
        curr_round_score   : tuple, holds the final scoring array and scoring check
        game_score         : int, final score of each game
        final_array        : bool array, final categories that had a score. True if was not scored. 
    
    """
    #Initialize arrays
    
    score_check = np.ones(13, dtype=bool)
    score_array = np.zeros(13)

    #Loop through thirteen rounds

    for k in range(0,len(score_check)):
        
        #Start with zero for all die
        die_array = np.zeros(5)

        #First roll and choices depending on roll
        die_array_one = fun.roll_dice(die_array)
        choices = fun.choice(die_array_one,score_check)
        
        #Second roll and choices depending on roll
        die_array_two = fun.roll_dice(choices[0])
        choices = fun.choice(die_array_two,score_check)
        
        #Third roll and choices depending on roll
        die_array_three = fun.roll_dice(choices[0])
        choices = fun.choice(die_array_three,score_check)
        
        #Final choice
        final_choice = choices[1]
    
        #Return final score and check arrays
        curr_round_score = fun.round_score(die_array_three,score_check,score_array,final_choice)
        #Final score for game
        game_score = np.sum(curr_round_score[0])
        #Final categories that were scored
        final_cat_array = curr_round_score[1]
        
    return (game_score,final_cat_array)

    
    