import math
import os

def  sin1(a,alpha,beta):
    return math.sin(beta)*a/math.sin(alpha)

def  sin2(a,b,alpha):
    return math.sin(alpha)*b/a

def tri(alpha,beta,gamma):
    return math.pi

def calangel(alpha,beta):
    return math.pi-alpha-beta

def s_p_1(a,b,c):
    p = sum([a,b,c])/3
    return math.sqrt(p*(p-a)*(p-b)*(p-c))
def s_p_2(s,a,b):
    return 