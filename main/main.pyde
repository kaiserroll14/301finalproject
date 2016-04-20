# 301 Final Project
# Cody Kaiser, Scott McGowan

# import requests
# import pandas
# import numpy
from requests import *
from pandas import *
from numpy import*

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

def draw_star(lst):
    beginShape()
    vertex(0, -50)
    vertex(14, -20)
    vertex(47, -15)
    vertex(23, 7)
    vertex(29, 40)
    vertex(0, 25)
    vertex(-29, 40)
    vertex(-23, 7)
    vertex(-47, -15)
    vertex(-14, -20)
    endShape(CLOSE)
    return


def draw_shape(lst):
    noStroke()
    if lst[1] == 1:
        fill(255,0,0)
    elif lst[1] == 2:
        fill(0,255,0)
    elif lst[1] == 3:
        fill(0,0,255)
    elif lst[1] == 4:
        fill(0,0,0)
    if lst[0] == 1:
        rect(lst[4],lst[4],lst[3],lst[3])
    elif lst[0] == 2:
        ellipse(lst[4],lst[4],lst[3],lst[3])
    elif lst[0] == 3:
        triangle(lst[4],lst[4],lst[4]+lst[3],lst[4]+lst[3],lst[4]-lst[3],lst[4]-lst[3])
    elif lst[0] == 4:
        draw_star()
    return


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
    size(1000, 1000)

    return

def draw():
    df = get_data(fname)
    for i in range(len(df)):
        draw_shape(df[i].values.tolist())
    return