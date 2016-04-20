# 301 Final Project
# Cody Kaiser, Scott McGowan

import requests

s = 50.0
m = 150.0
l = 250.0
xl = 350.0

def get_data():
    r = requests.get('http://52.38.78.108/data.php')
    data = r.content
    lst = []
    cpy = False
    for line in data.split():
        if line.strip() == '<p>':
            cpy = True
        elif line.strip() == '</p>':
            cpy = False
        elif cpy:
            lst.append(line[:4])
       
    return lst

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

def get_size(lst):
    siz = 0.0
    if lst[0] == 1:
        siz = s
    elif lst[0] == 2:
        siz = m
    elif lst[0] == 3:
        siz = l
    elif lst[0] == 4:
        siz = xl
    return siz

def get_POS(lst):
    x=0.0
    y=0.0
    if lst[0] == 1:
        x = random(1000)
        y = random(1000) 
    elif lst[0] == 2:
        x = random(1000)
        y = randrange(0,333.3)
    elif lst[0] == 3:
        x = random(1000)
        y = randrange(333.4, 666.6)
    elif lst[0] == 4:
        x = random(1000)
        y = randrange(666.7,1000)
    return (x,y)

def draw_shape(lst):
    noStroke()
    pos = get_POS(lst[3])
    siz = get_size(lst[2])
    if lst[1] == 1:
        fill(255,0,0)
    elif lst[1] == 2:
        fill(0,255,0)
    elif lst[1] == 3:
        fill(0,0,255)
    elif lst[1] == 4:
        fill(0,0,0)
    if lst[0] == 1:
        rect(pos[0],pos[1],siz,siz)
    elif lst[0] == 2:
        ellipse(pos[0],pos[1],siz,siz)
    elif lst[0] == 3:
        triangle(pos[0],pos[1],pos[0]+siz,pos[1]+siz,pos[0]-siz,pos[1]-siz)
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
    fill(126)
    size(1000, 1000)

    return

def draw():
    lst2 = get_data()
    for i in range(len(lst2)):
        draw_shape([int(j) for j in lst2[i]])
    return