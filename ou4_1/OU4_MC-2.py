#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Notebook used to approximate pi with a Monte Carlo - method. Perfect as I am taking BV2 along side this course.


# In[5]:


import random
from matplotlib import pyplot as plt


# In[6]:


import math


# In[7]:


import concurrent.futures as future
from time import perf_counter as pc


# In[4]:


# The idea is to generate random points in a square om side 1 using random.uniform(). By comparing how many of 
# these end up inside the unit circle to the total ammount we can approximate pi by this formula: pi = 4*(n_c/n)


# In[8]:


# Lambda to check if inside unit sphere of arbitrary dimension.
in_sphere = lambda point: sum(map(lambda x: x**2, point)) <= 1


# In[9]:


def getRandomPoints(n):
    '''n is the number of desired points.
    '''
    points = [0 for i in range(n)]
    for i in range(n):
        point = [random.uniform(-1,1), random.uniform(-1,1)]
        points[i] = point
    return points


# In[30]:


def timer(func):
    def wrapper(*args):
        start = pc()
        result = func(*args)
        print(f"Det tog: {pc() - start}")
        return result
    return wrapper


# In[23]:


# So, lets get to it:
def pi_mc(n, given_dist = None):
    '''Function approximating pi through 
    stochastics with n points
    ''' 
    points = getRandomPoints(n) if not given_dist else given_dist
    sphere_points = [in_sphere(point) for point in points]
    return 4*(sum(sphere_points)/n)


# In[24]:


def getAvgDistribution(n, m):
    '''n = number of avergages,
       m = number of random points in MC
    '''
    thsnd_avgs = []
    for i in range(n):
        thsnd_avgs.append(pi_mc(m))
    plt.hist(thsnd_avgs, 100)
    plt.show()


# In[57]:


# getAvgDistribution(100,100)


# In[12]:


# Function to plot random points 
def showPiPlot(n: int):
    '''n is the number of points to be
    plotted and used to calculate pi.
    '''
    points = getRandomPoints(n)
    ca_pi = pi_mc(n, points)
    
    fig, ax = plt.subplots()
    for point in points:
            clr = 'blue' if in_sphere(point) else 'red'
            ax.scatter(*point, color = clr)
    ax.set_title(f"This distribution gave the approxmation: pi = {ca_pi}")


# In[72]:


#showPiPlot(100)


# In[72]:



def MCVolume(n, d=10):
    ''' Function aprroximating volume of 
    d-dimensional sphere. 
    '''
    #n_c = 0 Part of commented solution below
    #for _ in range(n):
    
    #    I could do this: 
    #    if in_sphere(point):
    #        n_c += 1
    #    But since I should be using higher order functions
    #    I will be using filter.
    
    #   Brutal list comprehension
    points = [[random.uniform(-1,1) for _ in range(d)] for point in range(n)]
    n_c = len(list(filter(in_sphere, points)))
    # So, even though this looks complicated at first glance,
    # I would like to say it is pretty nice with 2 lines of code.
    
    # My thought is that the proportion of the
    # points ending up inside the sphere is equal
    # to the proportion between the unit d-dimensional
    # cube and sphere. Cube in this case has volume 2^d so
    # the formula below holds.
    return (2**d)*n_c/n


# In[14]:


def dSphereVolume(d):
    '''Analytical value of volume of 
    unit sphere in d dimensions'''
    return (math.pi**(d/2))/(math.gamma((d/2) + 1))


# In[35]:



def multiMCVolume(n, d, num_processes = 5):
    '''Function that uses multiprocessing to 
    calculate the voulme. Hopefully quicker than 
    the regular function.
    '''
    with future.ProcessPoolExecutor() as ex:
        points = n // num_processes
        p = [points for _ in range(num_processes)]
        # Compensate for uneven n
        p[0] += n % num_processes

        results = ex.map(MCVolume, p)
        # Take average of all results.
        return sum(results)/num_processes


# In[79]:


if __name__ == '__main__':
    start = pc()
    a = multiMCVolume(1000000, 11, 10)
    print(a, pc() - start)
    start = pc()
    a = MCVolume(1000000, 11)
    print(a, pc() - start)
