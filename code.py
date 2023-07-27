import numpy as np
import matplotlib
from matplotlib import style
import matplotlib.pyplot as plt

def first():
    return print("General Instructions:\n Give the equation in terms of x \n Give the triganometric equation without bracket ")

def plot(x,y):
    plt.plot(x,y,color='green',lw=0.5)
    plt.grid(True)
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.style.use('fivethirtyeight')
    plt.facecolor = 'yellow'
    return plt.show()

first()

x= np.linspace(-1,1)
a= int(input("press 1 if the equation is normal algebric \npress 2 if the the equation is triganometric\n "))
if a==1:
    eq=input("enter the equation in terms of x: ")
    y=eval(eq)
    plt.title(eq,color='blue')
    plot(x, y)
    
elif a == 2:
    eq=  input("enter the triganometric funtion: ")
    eq= eq.split()
    funtion = eq[0]
    equation = eq[1]
    print(funtion , equation)
    
else:
    print("invalid input")
    
try:
    
    equation= eval(equation)
    if funtion == 'sin':
        y= np.sin(equation)
        plot(x, y)
    elif funtion == 'cos':
            y= np.cos(equation)
            plot(x, y)
    elif funtion == 'tan':
        y= np.tan(equation)
        plot(x, y)
    else:
        print("invalid input")
    
except NameError:
    print("")
