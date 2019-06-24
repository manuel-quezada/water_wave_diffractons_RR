from numpy import genfromtxt
from matplotlib import pyplot as pl
import numpy as np

mwl = 0.75
g=9.8
ceff = np.sqrt(g*0.5)

def shift(x):
    # shift x-data due to the use of periodic BCs
    while sum(1.0*((x[1:]-x[0:-1])<0)) > 0:
        xArgShift = (1.0*((x[1:]-x[0:-1])<0)).argmax()+1 
        x[xArgShift:]+=100
    #
    # shift w.r.t. initial position
    x-=x[0]
#

# ******************************* #
# ********** READ DATA ********** #
# ******************************* #
wave1 = genfromtxt('wave1.txt',delimiter=' ')
x1=wave1[:,1]; t1=wave1[:,0]; w1=(wave1[:,2]).mean()-mwl; hu1=(wave1[:,3]).mean()
shift(x1)

# Wave 2
wave2 = genfromtxt('wave2.txt',delimiter=' ')
x2=wave2[:,1]; t2=wave2[:,0]; w2=(wave2[:,2]).mean()-mwl; hu2=(wave2[:,3]).mean()
shift(x2)

# Wave 3
wave3 = genfromtxt('wave3.txt',delimiter=' ')
x3=wave3[:,1]; t3=wave3[:,0]; w3=(wave3[:,2]).mean()-mwl; hu3=(wave3[:,3]).mean()
shift(x3)

# Wave 4
wave4 = genfromtxt('wave4.txt',delimiter=' ')
x4=wave4[:,1]; t4=wave4[:,0]; w4=(wave4[:,2]).mean()-mwl; hu4=(wave4[:,3]).mean()
shift(x4)

# Wave 5
wave5 = genfromtxt('wave5.txt',delimiter=' ')
x5=wave5[:,1]; t5=wave5[:,0]; w5=(wave5[:,2]).mean()-mwl; hu5=(wave5[:,3]).mean()
shift(x5)

# **************************************** #
# ********** compute velocities ********** #
# **************************************** #
v1 = ((x1[1:]-x1[0:-1])/(t1[1:]-t1[0:-1])).mean()
v2 = ((x2[1:]-x2[0:-1])/(t2[1:]-t2[0:-1])).mean()
v3 = ((x3[1:]-x3[0:-1])/(t3[1:]-t3[0:-1])).mean()
v4 = ((x4[1:]-x4[0:-1])/(t4[1:]-t4[0:-1])).mean()
v5 = ((x5[1:]-x5[0:-1])/(t5[1:]-t5[0:-1])).mean()

#################################
# ********** FITTING ********** #
#################################
amp = np.linspace(0,1.0)
vel = [v1, v2, v3, v4, v5] - ceff
# Linear fitting #
A=np.array([[w1-0],
            [w2-0],
            [w3-0],
            [w4-0],
            [w5-0]])
linear_fit = np.linalg.lstsq(A,vel)[0]
# quadratic
A=np.array([[w1**2-0**2, w1-0],
            [w2**2-0**2, w2-0],
            [w3**2-0**2, w3-0],
            [w4**2-0**2, w4-0],
            [w5**2-0**2, w5-0]])
quadratic_fit = np.linalg.lstsq(A,vel)[0]

pl.clf()
pl.xlim([0,0.1 ])
pl.ylim([ceff,2.4])
pl.plot(amp,linear_fit[0]*amp+ceff-linear_fit[0]*0,'-r',linewidth=3)
pl.plot(amp,quadratic_fit[0]*amp**2+quadratic_fit[1]*amp+ceff-quadratic_fit[0]*0**2-quadratic_fit[1]*0,'--k',linewidth=3)
pl.legend(['Linear fit','Quadratic fit'],loc=2,fontsize=20)
pl.gca().tick_params(labelsize=25)
pl.xlabel('Amplitude',fontsize=25)
pl.ylabel('Speed',fontsize=25)
pl.tight_layout()

pl.plot(0,ceff,'o', markerfacecolor='blue', markeredgecolor='blue', markeredgewidth=2, markersize=16)
pl.plot(w1.mean(),v1,'sb', markerfacecolor='none', markeredgecolor='blue', markeredgewidth=2, markersize=12)
pl.plot(w2.mean(),v2,'sb', markerfacecolor='none', markeredgecolor='blue', markeredgewidth=2, markersize=12)
pl.plot(w3.mean(),v3,'sb', markerfacecolor='none', markeredgecolor='blue', markeredgewidth=2, markersize=12)
pl.plot(w4.mean(),v4,'sb', markerfacecolor='none', markeredgecolor='blue', markeredgewidth=2, markersize=12)
pl.plot(w5.mean(),v5,'sb', markerfacecolor='none', markeredgecolor='blue', markeredgewidth=2, markersize=12)

pl.savefig('speed_waves.png')
