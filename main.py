import dynamics
import numpy as np
import scipy as sp
import drawer

#Simulation parameters
tf = 10000
t_max = 10

#System parameters
names = ['Alpha Centauri A','Alpha Centauri B','Proxima Centauri']
massCoefficient = np.array([1.1,0.91,0.1221])
solarMass = 1.989e30
mass = massCoefficient*solarMass

#States: [x1 y1 dx1 dy1 x2 y2 dx2 dy2 x3 y3 dx3 dy3].T
x0 =np.array([0,0,20000,10000,100000,100000,20000,10000, -200000, -50000, -15000,-10000, mass[0], mass[1], mass[2]])
x_t = np.hstack((0,x0))

#Evolution
# f = dynamics.dynamics(x0)
evolution = sp.integrate.RK45(dynamics.dynamics, 0, x0, tf, max_step=t_max)

while evolution.t < tf:
    evolution.step()
    entry = np.array(evolution.t)
    entry = np.hstack((entry, evolution.y))
    x_t = np.vstack((x_t,entry))
    # print(evolution.t)
    # print(evolution.y)

animator = drawer.animator(x_t, names)

print('hi this is yilong mah')