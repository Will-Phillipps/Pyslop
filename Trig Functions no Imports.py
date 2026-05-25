pi = 3.141592653589793 

#https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
#https://en.wikipedia.org/wiki/Euler_numbers#As_a_determinant

def factorial(x):
    if x == 0:
        return 1
    else:
        newx = 1
        for i in range(1,x+1):
            newx *= i
        return newx
    
def radtodeg(rad):
    deg = rad*(180/pi)
    return deg
        
def degtorad(deg):
    degfloat = float(deg)
    rad = degfloat*pi/180
    return rad
        
def sin(x,terms = 50):
    x = x % (2*pi)
    result = 0
    for n in range(terms):
        signvalue = ((-1)**n)
        value = (x**(2*n+1))/factorial(2*n+1)
        result += signvalue * value
    return round(result,10)
    
def cos(x, terms = 50):
    x = x % (2*pi)
    result = 0
    for n in range(terms):
        signvalue = ((-1)**n)
        value = (x**(2*n)) / factorial(2*n)
        result += signvalue * value
    return round(result,10)
    
def tan(x):
    result = 0
    result = sin(x)/cos(x)
    return round(result,10)
    
def sec(x):
    result = 0
    result = 1/cos(x)
    return round(result,10)

def arcsin(x,terms = 50):
    result = 0
    for n in range(terms):
        signvalue = factorial(2*n) * (x**(2*n+1))
        value = (4**n)*(factorial(n)**2)*(2*n+1)
        result += signvalue / value
    return round(result,10)
    
def arccos(x):
    result = 0
    result = (pi/2) - arcsin(x)
    return round(result,10)
    
def arctan(x,terms = 50):
    result = 0
    for n in range(terms):
        signvalue = ((-1)**n)*(x**(2*n+1))
        value = 2*n+1
        result += signvalue / value
    return round(result,10)
    
def sinh(x,terms = 50):
    result = 0
    for n in range(terms):
        signvalue = (x**(2*n+1))
        value = factorial(2*n+1)
        result += signvalue / value
    return round(result,10)

def cosh(x,terms = 50):
    result = 0
    for n in range(terms):
        signvalue = (x**(2*n))
        value = factorial(2*n)
        result += signvalue / value
    return round(result,10)
    
def tanh(x):
    result = 0 
    result = sinh(x)/cosh(x)
    return round(result,10)
    
def arsinh(x,terms = 50):
    result = 0
    for n in range(terms):
        signvalue = ((-1)**n)*factorial(2*n)*(x**(2*n+1))
        value = (4**n)*(factorial(n)**2)*(2*n+1)
        result += signvalue / value
    return round(result,10)
    
def artanh(x,terms = 50):
    result = 0
    for n in range(terms):
        signvalue = (x**(2*n+1))
        value = (2*n+1)
        result += signvalue / value
    return round(result,10)  #artanh
    
    
input1 = input("1 for sin \n2 for cos \n3 for tan\n4 for sec\n5 for arcsin\n6 for arccos\n7 for arctan\n8 for sinh\n9 for cosh\n10 for tanh\n11 for arsinh\n12 for artanh\ninput: ")

if input1 == "1":
    x = input("degrees as a whole number: ")
    try:
        xrad = degtorad(x)
    except:
        print("Invalid input")
        exit()
    print(f"approx sin({x}) = {sin(xrad)}")   #sin
    
elif input1 == "2":
    x = input("degrees as a whole number: ")
    try:
        xrad = degtorad(x)
    except:
        print("Invalid input")
        exit()
    print(f"approx cos({x}) = {cos(xrad)}")   #cos
    
elif input1 == "3":
    x = input("degrees as a whole number: ")
    try:
        xrad = degtorad(x)
    except:
        print("Invalid input")
        exit()
    c = cos(xrad)
    if abs(c) < 1e-12:
        print("Undefined (cos(x) = 0)")
        exit()    
    print(f"approx tan({x}) = {tan(xrad)}")   #tan
    
elif input1 == "4":
    ans = 0
    x = input("angle in degrees: ")
    try:
        xrad = degtorad(x)
    except:
        print("Invalid input")
        exit()  
    c = cos(xrad)
    if abs(c) < 1e-12:
        print("Undefined (cos(x) = 0)")
        exit()
    ans = sec(xrad)
    print(f"approx of sec({x}): {ans}")   #sec
        
elif input1 == "5":
    ans = 0
    x = input("ratio of o/h: ")
    try:
        xfloat = float(x)
    except:
        print(f"could not convert '{x}' to a float")
        exit()
    if xfloat < -1 or xfloat > 1:
        print("arcsin is only defined for -1 ≤ x ≤ 1")
        exit()
    ans = arcsin(xfloat)
    degans = radtodeg(ans)
    degans = round(degans,10)
    print(f"approx of arcsin({x}): \ndegrees: {degans}\nradians: {ans}")   #arcsin
    
elif input1 == "6":
    ans = 0
    x = input("ratio of a/h: ")
    try:
        xfloat = float(x)
    except:
        print(f"could not conver '{x}' to a float")
        exit()
    if xfloat < -1 or xfloat > 1:
        print("arccos is only defined for -1 ≤ x ≤ 1")
        exit()
    ans = arccos(xfloat)
    degans = radtodeg(ans)
    degans = round(degans,10)
    print(f"approx of arccos({x}): \ndegrees: {degans}\nradians: {ans}")   #arccos
    
elif input1 == "7":
    ans = 0
    x = input("ratio of o/a: ")
    try:
        xfloat = float(x)
    except:
        print(f"could not conver '{x}' to a float")
        exit()
    ans = arctan(xfloat)
    degans = radtodeg(ans)
    degans = round(degans,10)
    print(f"approx of arctan({x}): \ndegrees: {degans}\nradians: {ans}")  #arctan    #arctan
    
elif input1 == "8":    #sinh
    ans = 0
    x = input("scalar value: ")
    try:
        xfloat = float(x)
    except:
        print(f"could not convert '{x}' to a float")
        exit()
    ans = sinh(xfloat)
    print(f"approx of sinh({x}): {ans}")  #sinh  #sinh
    
elif input1 == "9":   #cosh
    ans = 0
    x = input("scalar value: ")
    try:
        xfloat = float(x)
    except:
        print(f"could not convert '{x}' to a float")
        exit()
    ans = cosh(xfloat)
    print(f"approx of cosh({x}): {ans}")  #cosh  #cosh
    
elif input1 == "10":    #tanh
    ans = 0
    x = input("scalar value: ")
    try:
        xfloat = float(x)
    except:
        print(f"could not convert '{x}' to a float")
        exit()
    ans = tanh(xfloat)
    print(f"approx of tanh({x}): {ans}")  #tanh
    
elif input1 == "11":
    ans = 0
    x = input("any real number: ")
    try:
        xfloat = float(x)
    except:
        print(f"could not convert '{x}' to a float")
        exit()
    ans = arsinh(xfloat)
    print(f"approx of arsinh({x}): {ans}")   #arsinh
    
elif input1 == "12":
    ans = 0
    x = input("any real number: ")
    try:
        xfloat = float(x)
    except:
        print(f"could not convert '{x}' to a float")
        exit()
    if abs(xfloat) >= 1:
        print("artanh is only defined for -1 < x < 1")
        exit()
    ans = artanh(xfloat)
    print(f"approx of artanh({x}): {ans}")  #artanh

