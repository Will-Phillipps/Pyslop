import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

orbit_radius = 500000 + 6371000 # 500 km above Earth's surface + Earth's radius
g = 6.674*10**-11      # Gravitational constant
m = 5.9722*10**24   # Mass of Earth
v = math.sqrt(g*m/orbit_radius)  # Orbital velocity in m/s
angular_velocity = math.sqrt(g*m/orbit_radius**3) # Angular velocity in rad/s
orbital_period = 2*math.pi/angular_velocity # Orbital period in seconds
x = 0
y = 0
orbiting_object_x_per_s = {}
orbiting_object_y_per_s = {}
orbiting_object_dict = {}
orbiting_object_dict = {x : orbiting_object_x_per_s, y : orbiting_object_y_per_s}

fig, ax = plt.subplots()
# min and max values for x and y axis
ax.set_aspect('equal', adjustable='box')
line, = ax.plot([], [], 'bo', markersize=6)  # 'bo' for blue circle marker

def initialize():
    ax.set_xlim(-orbit_radius*1.1, orbit_radius*1.1)
    ax.set_ylim(-orbit_radius*1.1, orbit_radius*1.1)
    line.set_data([], [])
    return line,

def animate(t):
    x = orbit_radius * math.cos(angular_velocity * t)
    y = orbit_radius * math.sin(angular_velocity * t)
    line.set_data([x], [y])
    return line,

# draw Earth for scale
earth = plt.Circle((0, 0), 6371000, color='tab:blue', alpha=0.3)
ax.add_patch(earth)

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=np.linspace(0, orbital_period, num=200),
    init_func=initialize,
    blit=True,
)

print(f"Orbital velocity: {v:.2f} m/s")
print(f"Angular velocity: {angular_velocity:.6f} rad/s")
print(f"Orbital period: {orbital_period:.2f} seconds")

#x and y cartesian coordinates of the satellite as a function of time

# x(t) = r * cos(angular_velocity * t + theta)   #theta is the intial angle in radians
# y(t) = r * sin(angular_velocity * t + theta)   #theta is set to 0 for ease of use

for t in range(0, int(orbital_period)+1):
    x = orbit_radius * math.cos(angular_velocity * t)
    y = orbit_radius * math.sin(angular_velocity * t)
    orbiting_object_x_per_s[t] = x
    orbiting_object_y_per_s[t] = y
    
print("Time (s) | X (m) | Y (m)")
for t in sorted(orbiting_object_x_per_s.keys()):
    print(f"{t:8} | {orbiting_object_x_per_s[t]:.2f} | {orbiting_object_y_per_s[t]:.2f}")
    
plt.title("Orbital Mechanics: Satellite Orbiting Earth")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.grid()
plt.show()
