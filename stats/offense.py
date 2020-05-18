import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games[games["type"] == "play"] #select all rows that have a 'type' of 'play'
#label columns
plays.columns= ['type','inning','team','player','count','pitches','event','game_id','year']

#distribution of hits across innings. just need the hits,singles,doubles,triples,home runs
#select rows where the 'event' column's value starts with
    #S (not SB); D; T; HR
#only return 'inning' and 'event' columns
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'),['inning','event']]
