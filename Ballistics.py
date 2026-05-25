import math
pi = math.pi
cd_dict = {
    "flat-face":1.28,
    "sphere":0.47,         #drag coefficients
    "airfoil/teardrop":0.07,
    "nosecone":0.14
}

p_dict = {
    "sealevelair":1.225,    #density of environment in kg/m^3
    "water":1000
}

'''
this is designed to be a simple ballisitics calculator, it is in no way accurate as i have no real data to compare it to,
i might add graphing with matplotlib at some point 
'''

def squarearea(a,b):
    area = a*b
    return area
   
def spherearea(pi,r):
    area = pi*(r**2)
    return area
   
def droporfoilarea(r,h):
    area = (pi*(r**2))/2 + (r*h)
    return area

def fastdragforce(cd,p,area,v):
    F_d = 0.5*cd*p*area*(v**2)
    return F_d
   
def slowdragforce(pi,mu,r,v):
    F_d = (6*pi)*mu*r*v
    return F_d
    
def getfastk():
    while True:
        shapeinput = input("1 for square/flat plane\n2 for sphere\n3 for nosecone/point\n4 for teardrop/airfoil\ninput:")
        shapeinput = shapeinput.strip().lower()
        shapeinput = int(shapeinput)
       
        if shapeinput == 1:
            a = float(input('side1 in m:'))
            b = float(input('side2 in m:'))
            area = squarearea(a,b)
            cd = cd_dict["flat-face"]
            break
        elif shapeinput == 2:
            r = float(input('radius in m:'))
            area = spherearea(pi,r)
            cd = cd_dict["sphere"]
            break
        elif shapeinput == 3:
            r = float(input('radius in m:'))
            area = spherearea(pi,r)
            cd = cd_dict["nosecone"]
            break
        elif shapeinput == 4:
            r = float(input("radius in m:"))
            h = float(input("height in m:"))
            area = droporfoilarea(r,h)
            cd = cd_dict["airfoil/teardrop"]
            break
        else:
            print("input is not one of the listed options, choose again")
        print(type(shapeinput))
    while True:
        envinput = int(input("1 for air at sea level\n2 for water\ninput:"))
        if envinput == 1:
            p = p_dict["sealevelair"]
            break
        elif envinput == 2:
            p = p_dict["water"]
            break
        else:
            print("input is not one of the given options")
    k = 0.5 * cd * p * area
    return k
   
initv = float(input("initial launch velocity in m/s:"))
deg = float(input("degrees of elevation from 0 deg:"))
theta = (pi/180) * deg
mass = float(input("mass in kg of object:"))
k = getfastk() # this needs to be pretty much the same as getfastdrag but wihtout speed so just all the shapes and env with no v
dt = 0.1 #time step
x = 0.0
y = 0.0
g = 9.8


vx = initv * math.cos(theta)
vy = initv * math.sin(theta)

xcoordlist, ycoordlist = [x], [y]

while y >= 0:
    v = math.sqrt((vx**2)+(vy**2))
    Fd = k * v*v
    ax = -(Fd/mass) * (vx/v)
    ay = -g - (Fd/mass) * (vy/v)
   
    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt
   
    xcoordlist.append(x)
    ycoordlist.append(y)
       

print(xcoordlist)
print(ycoordlist)
