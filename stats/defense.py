import pandas as pd
import matplotlib.pyplot as plt
#what is the defensive efficiency ration by league, since 1978
from frames import games, info, events

#query function to select all rows of 'games' dataframe
    #that have a 'type' of 'play' but do NOT have 'NP' as 'event'
plays = games.query("type == 'play' & event != 'NP' ")
