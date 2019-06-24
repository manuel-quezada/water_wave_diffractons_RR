import numpy as np
from matplotlib import pyplot as pl

N=1000
x=np.linspace(-1,1,N)

eta0=1.0
A=0.5
eta=eta0+A*np.exp(-(x)**2/0.04)

pl.figure(figsize=(15,10))

# Plot water surface
pl.plot(x,eta,'-b',linewidth=4)
pl.plot(x,x*0+eta0,'--r',linewidth=2)

xL=np.linspace(-1,-0.2,N)
xM=np.linspace(-0.2,0.3,N)
xR=np.linspace(0.3,0.8,N)
yB=np.linspace(0.5,0.75,N)

pl.plot(xL,0*xL+0.75,'-b',linewidth=2)
pl.plot(xM,0*xM+0.5,'-b',linewidth=2)
pl.plot(xR,0*xR+0.75,'-b',linewidth=2)
pl.plot(yB*0-0.2,yB,'-b',linewidth=2)
pl.plot(yB*0+0.3,yB,'-b',linewidth=2)

# Plot axes
pl.arrow(-1,0.5,0.15,0,color='k',head_width=0.03,head_length=0.03)
pl.arrow(-1,0.5,0,0.15,color='k',head_width=0.03,head_length=0.03)

# Plot arrows related to b
pl.arrow(0.5,0.61,0,0.11,color='k')
pl.arrow(0.5,0.61,0,-0.11,color='k')
pl.text(0.525,0.56, '$b$', fontsize=25)

# Plot arrows related to eta 
pl.arrow(0.875,0.75,0,0.22,color='k')
pl.arrow(0.875,0.75,0,0.22,color='k')
pl.arrow(0.875,0.75,0,-0.22,color='k')
pl.text(0.9,0.725, '$\eta_0$', fontsize=25)

# plots arrows related to h
pl.arrow(0.1,1,0,A*np.exp(-0.1**2/0.04)-0.03,color='k')
pl.arrow(0.1,1,0,-0.47,color='k')
pl.text(0.125,0.85, 'h', fontsize=25)

pl.arrow(-0.25,1,0,A*np.exp(-0.25**2/0.04)-0.03,color='k')
pl.arrow(-0.25,1,0,-0.22,color='k')
pl.text(-0.225,0.85, 'h', fontsize=25)

# plot point to indicate eta=h+b
pl.plot(0.225,1+A*np.exp(-0.225**2/0.04),"ob",markersize=10)
pl.text(0.25,1+A*np.exp(-0.225**2/0.04), '$\eta=h+b$', fontsize=25)

# plot arrows related to eps
pl.arrow(-0.75,eta0+A/2.,0,A/2.-0.03,color='k')
pl.arrow(-0.75,eta0+A/2.,0,-(A/2.-0.03),color='k')
pl.text(-0.74,eta0+A/2., '$\mathcal{O}(\epsilon)$', fontsize=25)
x=np.linspace(-0.85,-0.55,N)
pl.plot(x,x*0+eta0+A,'--r',linewidth=2)

# plot arrows related to lambda
pl.arrow(0,eta0+1.1*A,0.3-0.03,0,color='k')
pl.arrow(0,eta0+1.1*A,-0.3+0.03,0,color='k')
pl.text(-0.025,eta0+1.15*A, '$\lambda$', fontsize=25)

# control limits and axes 
pl.xlim([-1.1,1.0])
pl.ylim([-0.1,2.1])
pl.axis('off')
pl.gca().set_aspect('equal', adjustable='box')

# save figure
pl.savefig('notation.png')
