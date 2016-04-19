# 301 Final Project
# Cody Kaiser, Scott McGowan

import requests, gzip, os.path, types
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from bs4 import BeautifulSoup

'''
This function takes a file name requests it from the server to
get a file. From there we dump line by line(all values will be on sepereate lines)
into a dataframe to be later manipulated in other functions
'''
def get_data(fname):
    with open(fname, 'r') as fp:
        lst = json.load(fp)
    col = ['Color', 'Shape', 'Size', 'pos']
    arr = np.array(lst)
    return df.DataFrame(arr, col)

def get_user(df):
    makeShape = []
    data = df.values.tolist()
    for i 
    df.loc[[i]]
    
    return makeShape

'''
######################################################################################################################
                                                                                                                     #
88888888ba                                                                   88                         88           #
88      "8b                                                                  ""                         88           #
88      ,8P                                                                                             88           #
88aaaaaa8P' 8b,dPPYba,  ,adPPYba,   ,adPPYba,  ,adPPYba, ,adPPYba, ,adPPYba, 88 8b,dPPYba,   ,adPPYb,d8 88           #
88""""""'   88P'   "Y8 a8"     "8a a8"     "" a8P_____88 I8[    "" I8[    "" 88 88P'   `"8a a8"    `Y88 88           #
88          88         8b       d8 8b         8PP"""""""  `"Y8ba,   `"Y8ba,  88 88       88 8b       88 ""           #
88          88         "8a,   ,a8" "8a,   ,aa "8b,   ,aa aa    ]8I aa    ]8I 88 88       88 "8a,   ,d88 aa           #
88          88          `"YbbdP"'   `"Ybbd8"'  `"Ybbd8"' `"YbbdP"' `"YbbdP"' 88 88       88  `"YbbdP"Y8 88           #
                                                                                             aa,    ,88              #
                                                                                              "Y8bbdP"               #  
                                                                                                                     #                                                                                                                     #
######################################################################################################################                                                                                              
'''
def setup():
    size(500, 500)

    return

def draw():
    
    return