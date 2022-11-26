import math
import numpy as np
import os

def  sin1(a,alpha,beta):
    return math.sin(beta)*a/math.sin(alpha)

def  sin2(a,b,alpha):
    return math.sin(alpha)*b/a

def tri_1(alpha,beta,gamma):
    return math.pi

def tri_2(alpha,beta):
    return math.pi-alpha-beta

def s_p_1(a,b,c):
    p = sum([a,b,c])/3
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def s_p_2_1(c,hc):
    return c*hc/2

def s_p_2_2(s,x):
    return 2*s/x 

def init_network(num_func, num_para):
    return np.zeros((num_para,num_func))-1