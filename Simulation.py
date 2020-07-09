"""
Purpose : Simulate N games of Yahtzee and perform analysis. 
    
Created on 27/6/2020
@author: Murray Keogh

Program description: 
    Using the Play_Game script, simulate N games of Yahtzee and then perform 
    analysis on the results. 
   
Function dictionary:
    
   simulations         : Number of games to simulate. 
   scores              : Array to hold score of each full game. 
   cat_counter         : Array to hold counter of how many times a given category did not recieve a score during a game
   
   
"""
import numpy as np
import Play_Game as pg
import matplotlib.pyplot as plt
import seaborn as sns

#Initialize simulation number and arrays
simulations = 100
scores = np.zeros(simulations)
cat_counter = np.zeros(13)

#Loop through number of simulations
for k in range(0,len(scores)):
    
    #Play a game
    x = pg.play_game()
    
    #Return the array with categories scored
    cat_round = x[1]
    
    #Update scores array with final game score
    scores[k] = x[0]
    
    #Update the cat_counter array with categories not scored during this game
    for i in range(0,len(cat_counter)):
        if cat_round[i]:
            cat_counter[i] = cat_counter[i]+1
       
#Print average and category counter
print(np.mean(scores))
print(cat_counter)

    
# Density Plot and Histogram of scores
sns.distplot(scores, hist=True, kde=True,
             color = 'darkblue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})

#Bar chart for category counter

fig = plt.figure(figsize=(20,4))
ax = fig.add_axes([0,0,1,1])
ax.set_xlabel('Scoring Category')
ax.set_ylabel('Number of Games with No Score')
ax.set_title('Breakdown of Scoring Category - Games with No Score')
category = ['One', 'Two', 'Three', 'Four', 'Five','Six','Three of a Kind','Four of a Kind','Small Straight','Large Straight','Full House','Yahtzee','Chance']
ax.bar(category,cat_counter)
plt.show()

