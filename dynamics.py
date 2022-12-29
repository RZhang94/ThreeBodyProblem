import numpy as np
import scipy as sp

#Dynamics
def dynamics(t,x):
    g = 6.6743e-11
    m1, m2, m3 = x[12], x[13], x[14]

    r1 = np.array([[x[0]],[x[1]]])
    r2 = np.array([[x[4]],[x[5]]])
    r3 = np.array([[x[8]],[x[9]]])

    dr1 = np.array([[x[2]],[x[3]]])
    dr2 = np.array([[x[6]],[x[7]]])
    dr3 = np.array([[x[10]],[x[11]]])

    r12 = r1 - r2
    r13 = r1 - r3
    r23 = r2 - r3
    r12_norm =np.linalg.norm(r12)
    r13_norm =np.linalg.norm(r13)
    r23_norm =np.linalg.norm(r23)
    if r12_norm < 1e-3:
        r12_norm = 0
        r12 = 1e-3
    if r23_norm < 1e-3:
        r23_norm = 0
        r23 = 1e-3
    if r13_norm < 1e-3:
        r13_norm = 1e-3
        r13 = 0
    ddr1 = -g*m2*r12/(r12_norm)**3 - g*m3*r13/(r13_norm)**3
    ddr2 = -g*m3*r23/(r23_norm)**3 + g*m1*r12/(r12_norm)**3
    ddr3 = g*m1*r13/(r13_norm)**3 + g*m2*r23/(r23_norm)**3

    returnArray = np.array([dr1[0],dr1[1], ddr1[0], ddr1[1],dr2[0],dr2[1], ddr2[0], ddr2[1],dr3[0],dr3[1], ddr3[0], ddr3[1], [0], [0], [0]]).flatten()
    return returnArray

