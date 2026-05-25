import math

pdict = {}
normpdict = {}
def getpoints():
    global pdict,normpdict
    input1 = int(input("n of points: "))
    for x in range(input1):
        xinput = int(input(f"point{x} x:"))
        yinput = int(input(f"point{x} y:"))
        pdict[f"point{x}"]={"x":xinput,"y":yinput}
    normpdict = {k: v.copy() for k, v in pdict.items()}

def move():
    global pdict
    print("to move down(y) input negative value\nto move left(x) input negative value\nto move right(x) input positive value\nto move up(y) input positive value")
    dirinput = input("move on x or y: ").strip().lower()
    if dirinput == "x":
        xmoveamount = int(input("how much to move: "))
        for k,v in pdict.items():
            v["x"] += xmoveamount
    elif dirinput == "y":
        ymoveamount = int(input("how much to move: "))
        for k,v in pdict.items():
            v["y"] += ymoveamount        
    else:
        print("invalid input choose either x or y")
       
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
   
    for k,v in pdict.items():
        x = v["x"]
        y = v["y"]
       
        gx = scale_x(x)
        gy = scale_y(y)
       
        row = (height - 1)-y
        col = x
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = '*'
       
    for row in grid:
        print(''.join(row))
       
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
        move()
    elif cmd == "plot":
        pass
    elif cmd == "quit":
        break
    else:
        print("Unknown command.")
        continue

    plot()