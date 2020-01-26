import os
import pandas as pd
import magic



# import argparse
# parser = argparse.ArgumentParser()
# f = parser.parse_args()

def analyze(f):
    #magic.from_file(f)
    df = pd.read_csv('../../media/' + f)
    print('la la la')
    return(len(df))
    # return(magic.from_file(f))

def get_dtype(f):
    df = pd.read_csv(f)
    print(df.info())
    # return(df.info())


# functions to define

# if it is categorical or numeric data
# is it 1 and 0 data do we need propotions test?
# is data normally distribute
#

