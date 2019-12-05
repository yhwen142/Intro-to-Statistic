#Write 
from math import sqrt

def mean(l):
    return float(sum(l))/len(l)

def var(l):
    m = mean(l)
    return sum([(x-m)**2 for x in l])/len(l)

def factor(l):
    return 1.96


def conf(l):
    #Insert your code here
    return factor(l)*sqrt(var(l)/len(l))