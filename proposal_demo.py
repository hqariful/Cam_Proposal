import numpy as np
import matplotlib.pyplot as plt

outStroke = 60
dwell = 30
rtnStroke = 60
rBase = 50
maxDisp = 40

# creating variable for angle 
theta = np.linspace(0,360,360)

# similarly creating radius variable
# and initializing with 0
r = np.zeros(np.shape(theta))

r[outStroke:outStroke+dwell] = maxDisp
r[:outStroke] = theta[:outStroke]/outStroke*maxDisp
r[outStroke+dwell:outStroke+dwell+rtnStroke] = maxDisp - theta[:rtnStroke]/rtnStroke*maxDisp

fig = plt.figure()
def disp_diag():
    ax = fig.add_subplot()
    ax.plot(theta,r)
    ax.grid(True)

def radial_plot():
    rtheta = np.pi/180 * theta
    ax_r = fig.add_subplot(projection = 'polar')
    ax_r.plot(rtheta,r+rBase)
    ax_r.set_theta_offset(np.pi/2)

radial_plot()
plt.show()