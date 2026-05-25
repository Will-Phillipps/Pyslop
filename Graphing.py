import math

pdict = {}
normpdict = {}
transdict = {"x":0,"y":0}

def getcoords(input1,xmoveamount):
    global pdict,normpdict
    start, end = -(input1/2)+xmoveamount,(input1/2)+1+xmoveamount
    start, end = int(start),int(end)
    for x in range(start,end):
        xinput = x/10
        yinput = math.sin(x/10)
        pdict[f"point{x}"]={"x":xinput,"y":yinput}
    normpdict = {k: v.copy() for k, v in pdict.items()}  

def getpoints():
    global input1
    input1 = int(input("n of points determines limits of x which also determines the tightness of the graph\nn of points: "))
    getcoords(input1,0)

def move():
    global pdict, transdict,xmoveamount
    print("moving on x changes your view of the graph, moving on y changes the position of the graph on the y-axis")
    print("to move left(x) input negative value\nto move right(x) input positive value\nto move up(y) input positive valu\nto move down(y) input negative value\nvalues are done at a 10:1 ration if you input 10 it will move your view by 1 coordinate e.g an input of 10 on x will change the min by +1 and the max by +1 (-1,1) -> (0,2)")
    dirinput = input("move on x or y: ").strip().lower()
    if dirinput == "x":
        xmoveamount = int(input("how many units to move: "))
        transdict["x"] += xmoveamount
        getcoords(input1,transdict["x"])
    elif dirinput == "y":
        ymoveamount = int(input("how many units to move: "))
        transdict["y"] += ymoveamount
        getcoords(input1,transdict["x"])
    else:
        print("invalid input, choose x or y")
       
def reset():
    global pdict
    pdict = {k: v.copy() for k, v in normpdict.items()}

def cleardicts():
    pdict.clear()
    normpdict.clear()
   
def plot():
    width = 60
    height = 20
    if not pdict:
        print("No points to plot.")
        return

    xcoords = [v["x"] for v in pdict.values()]
    ycoords = [v["y"] for v in pdict.values()]
   
    xmin, xmax = min(xcoords),max(xcoords)
    ymin, ymax = min(ycoords),max(ycoords)
   

    def scale_x(x):
        if xmax == xmin:
            return 0
        return int((x - xmin) / (xmax - xmin) * (width - 1))

    def scale_y(y):
        if ymax == ymin:
            return 0
        return int((y - ymin) / (ymax - ymin) * (height - 1))

   
    grid = [[' ' for _ in range(width)] for _ in range(height)]
   
    if ymin <= 0 <= ymax:
        gy0 = scale_y(0)
        row0 = (height - 1) - gy0
        for col in range(width):
            grid[row0][col] = '-'

    if xmin <= 0 <= xmax:
        gx0 = scale_x(0)
        col0 = gx0
        for row in range(height):
            grid[row][col0] = '|'
   
    for k,v in pdict.items():
        x = v["x"]
        y = v["y"]
       
        gx = scale_x(x)
        gy = scale_y(y)
       
        row = (height - 1)-gy
        col = gx
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = '*'
       
    for row in grid:
        print(''.join(row))
       
    print(f"xmin: {xmin} , xmax: {xmax}\nymin: {ymin} , ymax {ymax}")
   
    for k,v in transdict.items():
        xtrans = transdict.get("x")  
        ytrans = transdict.get("y")
   
    if xtrans != 0:
        print(f"Translated by {xtrans} on the x-axis")
    elif ytrans != 0:
        print(f"Translated by {ytrans} on the y-axis")
    else:
        pass
   
getpoints()
plot()

while True:
    cmd = input("\nCommand (modify/reset/move/plot/quit): ").strip().lower()
    if cmd == "modify":
        cleardicts()
        getpoints()
    elif cmd == "reset":
        reset()
    elif cmd == "move":
        cleardicts()
        move()
    elif cmd == "plot":
        pass
    elif cmd == "quit":
        break
    else:
        print("Unknown command.")
        continue

    plot()