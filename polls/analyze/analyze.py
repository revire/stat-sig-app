import os
import pandas as pd

def analyze(f):
    df = pd.read_csv(f)
    return(len(df))

# functions to define

# if it is categorical or numeric data
# is it 1 and 0 data do we need propotions test?
# is data normally distribute
#

