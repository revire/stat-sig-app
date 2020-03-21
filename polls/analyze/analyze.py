import os
import pandas as pd
import magic
import os


# import argparse
# parser = argparse.ArgumentParser()
# f = parser.parse_args()

print('hey yo')


def analyze(f):

    df = pd.read_csv(f)
    length = len(df)
    visitors = df['visitors']
    clickers = df['clicker3']
    button = df['button']
    no = df['no']
    visitors_type = visitors.dtype
    clickers_type = clickers.dtype
    button_type = button.dtype
    no_type = no.dtype
    return(visitors_type, clickers_type, button_type, no_type)







d = 'dataset.csv'
print(analyze(d))


# functions to define

# if it is categorical or numeric data
# is it 1 and 0 data do we need propotions test?
# is data normally distribute
#

