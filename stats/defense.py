import pandas as pd
import matplotlib.pyplot as plt
#what is the defensive efficiency ration by league, since 1978
from frames import games, info, events

#query function to select all rows of 'games' dataframe
    #that have a 'type' of 'play' but do NOT have 'NP' as 'event'
plays = games.query(" type == 'play' & event != 'NP' ")
#adjust/rename column labels
plays.columns = ['type','inning','team','player','count','pitches',
                 'event','game_id','year']

#remove consecutive duplicate rows that represent the same at bat
    #shift() moves the index a specified amount up or down
#select all Rows that do Not match a consecutive row in the player column
#keep only a few specified columns
pa = plays.loc[plays['player'].shift() != plays['player'] ,
               ['year','game_id','inning','team','player']]
