#functions for picking random ship positions
from random import randint

def random_orientation():
    return randint(0,1)

def determ_ship_space(length,size):
    poss_ship_space=[]
    orient=random_orientation()
    if orient==0:
        for x in range(size):
            poss_ship_space.append(["@"]*(size-length+1))
    else:
        for x in range((size-length+1)):
            poss_ship_space.append(["@"]*size)
    start_row=random_row(poss_ship_space)
    start_col=random_col(poss_ship_space)
    
    ship_space=[]
    for i in range(length):
        if orient==0:
            ship_space.append([start_row,start_col+i])
        if orient==1:
            ship_space.append([start_row+i,start_col])
    return ship_space
            

def random_row(ship_space):
    return randint(0, len(ship_space) - 1)

def random_col(ship_space):
    return randint(0, len(ship_space[0]) - 1)