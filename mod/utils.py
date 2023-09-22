import math
import random

def mt_sqrt(x):
    return math.sqrt(x)

def mt_sinpi():
    return math.sin(math.pi / 2)

def mt_elog():
    return math.log(math.e)

def mt_exp(x):
    return math.exp(x)

def mt_pi():
    return math.pi
    
    
def rd_randrange(x, y):
    return random.randrange(x, y)

def rd_choice(this):
    return random.choice(this)

def rd_random():
    return random.random()

def rd_normalvariate():
    return random.normalvariate(0.1)
