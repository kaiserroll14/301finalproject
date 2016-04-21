# 301 Final Project
# Cody Kaiser, Scott McGowan

import requests
import random

s = 50.0
m = 150.0
l = 250.0
xl = 350.0

shapes = []

class my_shape(lst):
    def __init__(self, lst):
        self.shape_type = lst[0]
        self.shape_col = lst[1]
        self.shape_size = lst[2]
        self.shape_pos = lst[3]
        return
    
    def shape_draw():
        if self.shape_type == 1:
            rect(pos[0],pos[1],siz,siz)
        elif self.shape_type == 2:
            ellipse(pos[0],pos[1],siz,siz)
        elif self.shape_type == 3:
            triangle(pos[0],pos[1],pos[0]+siz,pos[1]+siz,pos[0]-siz,pos[1]-siz)
        elif self.shape_type == 4:
            draw_star()
        return


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


def draw_star():
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


def get_size(num):
    siz = 0.0
    if num == 1:
        siz = s
    elif num == 2:
        siz = m
    elif num == 3:
        siz = l
    elif num == 4:
        siz = xl
    return siz


def get_POS(num):
    x=0.0
    y=0.0

    if num == 1:
        x = round(random.random()*1000, 2)
        y = round(random.random()*1000, 2) 
    elif num == 2:
        x = round(random.random()*1000, 2)
        y = float(random.randrange(0,333))
    elif num == 3:
        x = round(random.random()*1000, 2)
        y = float(random.randrange(334, 666))
    elif num == 4:
        x = round(random.random()*1000, 2)
        y = float(random.randrange(667,1000))
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


def setup():
    fill(126)
    size(1000, 1000)
    return


def draw():
    lst2 = get_data()
    for i in range(len(lst2)):
        draw_shape([int(j) for j in lst2[i]])
    return
