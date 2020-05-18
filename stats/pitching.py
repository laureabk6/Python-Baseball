import pandas as pd
import matplotlib.pyplot as plt
from data import games

#condense the data to just rows of type play
#games[] : shortcut to access the dataframe games
#check if the 'type' column's value equals 'play'
#select just the rows that have a 'type' of 'play'
#type is a column
plays = games[games['type'] == 'play']
#select all rows that contain 'K' in 'event' column
strike_outs = plays[plays['event'].str.contains('K')]
#group the strike_outs dataframe by year and then by game_id
strike_outs = strike_outs.groupby(['year','game_id']).size()
