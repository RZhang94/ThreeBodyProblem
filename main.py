import dynamics
import numpy as np
import scipy as sp

#Simulation parameters
tf = 10
# ti = 100
# t = np.arange(0,tf, ti)

#System parameters
names = ['Alpha Centauri A','Alpha Centauri B','Proxima Centauri']
massCoefficient = np.array([1.1,0.91,0.1221])
solarMass = 1.989e30
mass = massCoefficient*solarMass

#States: [x1 y1 dx1 dy1 x2 y2 dx2 dy2 x3 y3 dx3 dy3].T
x0 =np.array([0,0,0,0,10000,10000,0,0, -20000, -5000, 0,0, mass[0], mass[1], mass[2]])

#Evolution
# f = dynamics.dynamics(x0)
evolution = sp.integrate.RK45(dynamics.dynamics, 0, x0, tf)

print('hi this is yilong mah')