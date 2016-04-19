# 301 Final Project
# Cody Kaiser, Scott McGowan

import requests, gzip, os.path

'''
This function takes a file name requests it from the server to
get a file. From there we dump line by line(all values will be on sepereate lines)
into a list to be later manipulated in other functions
'''
def get_data(fname):
    with open(fname) as f:
        content = f.readlines()
    return content

'''
Sorts the jumbled up shit heap that the list we made in get_data into 
the sperate data categories that we are looking for... 

IE: Color, Size, Shape, Randomness, Lines, How Many
'''
def sort_list(lst):
    colors = []
    size = []

    for i in lst:
        if i == 'Red' or i == 'Blue':
            colors.append(i)
        elif i.isdigit():
            size.append(i)


'''
Pulls the Colors from our sort_list and returns a string of the most 
voted for color
'''
def get_color(lst):
    
    color = ????
    return color


'''
Pulls the booleans for randomness and returns whether or not the majority
of the class wants the elements to be given randomness to their position
'''
def get_Rando(lst):
    return

'''
'''
def get_shape(lst):
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
    size(500, 500)
    return

def draw():
    
    return