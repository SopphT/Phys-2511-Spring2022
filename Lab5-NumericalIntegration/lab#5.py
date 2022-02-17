#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 14:50:40 2022

@author: sopyt
"""
#this code is so long!! but it makes sense to me written this way for now
#Three curves 
#INPUT: Widths of rectangles (delta x)

#height = y value at any given point in rectangle (rectangle rule)
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci

def straight_line(x):
    return -0.5*x + 4.0


def parabola(x):
    return -0.29*x*x - x + 12.5


def comp_func(x):
    return(1.0 + 10*(x+1.0)*np.exp(-x*x))

rec_width = float(input("How wide are the rectangles going to be? "))

def integral_func(function):
    
    counter = -5.0

    integral = 0 
    
    while counter < 5.0:
        area = rec_width * function(counter)
        counter = counter + rec_width
        integral = integral + area

    return integral

print("\nFor the straight line function:\n") #these print statements probably do not need to be so ...much

print("\tIntegral of the straight line function:", integral_func(straight_line))
print("\tPercent difference from true area:", (integral_func(straight_line)-(40.0))/40.0 * 100)

print("\tThe SciPy Value is:", sci.quadrature(straight_line,-5,5))

print("\nFor the parabola function:\n")

print("\tIntegral of the parabola function:", integral_func(parabola))
print("\tPercent difference from true area:", (integral_func(parabola)-(100.83))/100.83 * 100)

print("\tThe SciPy Value is:", sci.quadrature(parabola,-5,5))

print("\nFor the more complicated function:\n")

print("\tInteral of the complicated function:", integral_func(comp_func))
print("\tPercent difference from true area:", (integral_func(comp_func)-(27.72))/27.72 * 100)

print("\tThe SciPy Value is:", sci.quadrature(comp_func,-5,5))


rec_width = 0.0001

rec_width_data = []
percent_diff_data = []

#probably some way to condense these while loops for plotting

while rec_width < 1:
    rec_width = rec_width + 0.001
    percent_diff =  (integral_func(straight_line)-(40.0))/40.0 * 100
    rec_width_data.append(rec_width)
    percent_diff_data.append(percent_diff)

plt.plot(rec_width_data,percent_diff_data)
plt.xlabel("Rectangle Width")
plt.ylabel("Percent Difference")
plt.title("How Percent Difference Changes With Rectangle Width - Straight Line")
plt.show()

rec_width = 0.0001

rec_width_data = []
percent_diff_data = []

while rec_width < 1:
    rec_width = rec_width + 0.001
    percent_diff = (integral_func(parabola)-(100.83))/100.83 * 100
    rec_width_data.append(rec_width)
    percent_diff_data.append(percent_diff)

plt.plot(rec_width_data,percent_diff_data)
plt.xlabel("Rectangle Width")
plt.ylabel("Percent Difference")
plt.title("How Percent Difference Changes With Rectangle Width - Parabola Line")
plt.show()

rec_width = 0.0001

rec_width_data = []
percent_diff_data = []

while rec_width < 1:
    rec_width = rec_width + 0.001
    percent_diff = (integral_func(comp_func)-(27.72))/27.72 * 100
    rec_width_data.append(rec_width)
    percent_diff_data.append(percent_diff)

plt.plot(rec_width_data,percent_diff_data)
plt.xlabel("Rectangle Width")
plt.ylabel("Percent Difference")
plt.title("How Percent Difference Changes With Rectangle Width - Complicated Function")
plt.show()

