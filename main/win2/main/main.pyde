# 301 Final Project
# Cody Kaiser, Scott McGowan

import requests
import random

shapes = []

class my_shape():
    def __init__(self, lst):
        lst = [int(i) for i in lst]
        lst = list(lst)
        self.shape_type = lst[0]
        self.shape_col = self.get_color(lst[1])
        self.shape_size = self.get_size(lst[2])
        self.shape_pos = self.get_pos(lst[3])
        return

    def get_string(self):
        result = "{} {} {} {}".format(self.shape_type, self.shape_col, self.shape_size, self.shape_pos)
        return result
    
    def shape_draw(self):
        fill(self.shape_col[0], self.shape_col[1], self.shape_col[2])

        if self.shape_type == 1:
            rect(self.shape_pos[0], self.shape_pos[1],
                 self.shape_size, self.shape_size)
        elif self.shape_type == 2:
            ellipse(self.shape_pos[0], self.shape_pos[
                    1], self.shape_size, self.shape_size)
        elif self.shape_type == 3:
            x1 = self.shape_pos[0]
            y1 = self.shape_pos[1]
            x2 = self.shape_pos[0] + (self.shape_size/2)
            y2 = self.shape_pos[1] - (self.shape_size/1.5)
            x3 = self.shape_pos[0] + self.shape_size
            y3 = self.shape_pos[1]
            triangle(x1, y1, x2, y2, x3, y3)
        elif self.shape_type == 4:
            self.draw_star()
        return

    def get_size(self, num):
        siz = 0.0
        if num == 1:
            siz = 50.0
        elif num == 2:
            siz = 150.0
        elif num == 3:
            siz = 250.0
        elif num == 4:
            siz = 350.0
        return siz

    def get_pos(self, num):
        x = 0.0
        y = 0.0
        if num == 1:
            x = round(random.random() * 1000, 2)
            y = round(random.random() * 1000, 2)
        elif num == 2:
            x = round(random.random() * 1000, 2)
            y = float(random.randrange(0, 333))
        elif num == 3:
            x = round(random.random() * 1000, 2)
            y = float(random.randrange(334, 666))
        elif num == 4:
            x = round(random.random() * 1000, 2)
            y = float(random.randrange(667, 1000))
        return (x, y)

    def draw_star(self):
        x = self.shape_pos[0]
        y = self.shape_pos[1]
        siz = self.shape_size / 100
        beginShape()
        vertex(x + (47 * siz), y + (0 * siz))
        vertex(x + (61 * siz), y + (30 * siz))
        vertex(x + (94 * siz), y + (35 * siz))
        vertex(x + (70 * siz), y + (57 * siz))
        vertex(x + (76 * siz), y + (90 * siz))
        vertex(x + (47 * siz), y + (75 * siz))
        vertex(x + (18 * siz), y + (90 * siz))
        vertex(x + (24 * siz), y + (57 * siz))
        vertex(x + (0 * siz), y + (35 * siz))
        vertex(x + (33 * siz), y + (30 * siz))
        endShape(CLOSE)
        return

    def get_color(self, num):
        if num == 1:
            return (255, 0, 0)
        if num == 2:
            return (0, 255, 0)
        if num == 3:
            return (0, 0, 255)
        if num == 4:
            return (0, 0, 0)


####################
# Begin Processing #
####################


def setup():
    noStroke()
    background(255, 255, 255)
    size(1000, 1000)
    
    data = get_data()
    for row in data:
        print(row)
        shapes.append(my_shape(row))
    return


def draw():
    data = get_data()

    if len(data) > len(shapes):
        for i in range(len(shapes), len(data)):
            print(data[i])
            shapes.append(my_shape(data[i]))
    
    for shape in shapes:
        shape.shape_draw()
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
            for item in line.split("<br>"):
                if item[:4].isdigit():
                    lst.append(item[:4])
    return lst