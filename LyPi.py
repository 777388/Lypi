from decimal import Decimal
from decimal import getcontext
import sys
import re
import matplotlib.pyplot as plt

#https://medium.com/@HeCanThink/pi-exploring-the-digits-of-pi-using-python-224d20937185
def pi(precision):
    getcontext().prec=precision
    return sum(1/Decimal(16)**k * 
        (Decimal(4)/(8*k+1) -
         Decimal(2)/(8*k+4) -
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)) for k in range(precision))
    
#For Bits and Biggles
#def pi(precision):
    getcontext().prec=precision
    return str(sum(1/Decimal(16)**k * 
        (Decimal(4)/(8*k+1) -
         Decimal(2)/(8*k+4) -
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)) + " ") for k in range(precision))

bing = str(pi(int(sys.argv[1])))
r = []
for char in bing:
    if char.isnumeric():
        r.append(int(char))
b = []
with open(sys.argv[2], 'r') as f:
    for bing in f:
        for char in bing:
            if ord(char) % 10 == 0:
                b.append(ord(char) - r.index(ord(char) % 10))
            if ord(char) % 10 == 1:
                b.append(ord(char) - r.index(ord(char) % 10) + 1)
            if ord(char) % 10 == 2:
                b.append(ord(char) - r.index(ord(char) % 10) + 2)
            if ord(char) % 10 == 3:
                b.append(ord(char) - r.index(ord(char) % 10) + 3)
            if ord(char) % 10 == 4:
                b.append(ord(char) - r.index(ord(char) % 10) + 4)
            if ord(char) % 10 == 5:
                b.append(ord(char) - r.index(ord(char) % 10) + 5)
            if (ord(char) % 10 == 6):
                b.append(ord(char) - r.index(ord(char) % 10) + 6)
            if (ord(char) % 10 == 7):
                b.append(ord(char) - r.index(ord(char) % 10) + 7)
            if (ord(char) % 10 == 8):
                b.append(ord(char) - r.index(ord(char) % 10) + 8)
            if (ord(char) % 10 == 9):
                b.append(ord(char) - r.index(ord(char) % 10) + 9)

g = lambda g: g - g / g
plt.plot(list(map(g, b)))
plt.show()



