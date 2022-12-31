import dynamics
import numpy as np
import scipy as sp
import drawer

#Simulation parameters
tf = 3e7 * 2e2 #years
t_max = 2.5e6

#System parameters
names = ['Alpha Centauri A','Alpha Centauri B','Proxima Centauri']
massCoefficient = np.array([2,1,1])
solarMass = 1.989e30
mass = massCoefficient*solarMass

#States: [x1 y1 dx1 dy1 x2 y2 dx2 dy2 x3 y3 dx3 dy3].T
body1p = np.array([0,1])*1e12
body1v = np.array([0,0])*1e3
body2p = np.array([-1,-1])*1e12
body2v = np.array([-2,-1])*1e3
body3p = np.array([1,-1])*1e12
body3v = np.array([-4,4])*1e3
x0 =np.hstack((body1p, body1v, body2p, body2v, body3p, body3v, mass))
x_t = np.hstack((0,x0))

#Evolution
# f = dynamics.dynamics(x0)
evolution = sp.integrate.RK45(dynamics.dynamics, 0, x0, tf, max_step=t_max)

while evolution.t < tf:
    evolution.step()
    entry = np.array(evolution.t)
    entry = np.hstack((entry, evolution.y))
    x_t = np.vstack((x_t,entry))

animator = drawer.animator(x_t, names)
animator.createAnimation()
print('hi this is yilong mah')