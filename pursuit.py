import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

pi = math.pi

targetinitpos  = (500,1000)
chaserinitpos   = (0,0)

initx1 = targetinitpos[0]
initx2 = chaserinitpos[0]
inity1 = targetinitpos[1]
inity2 = chaserinitpos[1]

initxgroup = (initx2-initx1)**2
initygroup = (inity2 - inity1)**2

initdistance = math.sqrt(initxgroup + initygroup)

chaservel = 80
targetvel = 50

initangle = math.atan(targetinitpos[0]/targetinitpos[1])

x1 = initx1
x2 = initx2
y1 = inity1
y2 = inity2
angle = initangle
dist = initdistance

chaserx = []
chasery = []
targetx = []
targety = []

while dist > 100:
    dist = dist - chaservel
    x1 += targetvel 
    y1 += 0
    x2 = x2 + chaservel * math.sin(angle)
    y2 = y2 + chaservel * math.cos(angle)
    angle = math.atan((x1-x2)/(y1-y2))
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    chaserx.append(x2)
    chasery.append(y2)
    targetx.append(x1)
    targety.append(y1)
    
plt.plot(chaserx, chasery, label='Chaser')
plt.plot(targetx, targety, label='Target')    
plt.xlim(0, chaserx[-1]+100)
plt.ylim(0, targety[-1]+100)
plt.title('Pursuit Curve')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.legend()
plt.show()
