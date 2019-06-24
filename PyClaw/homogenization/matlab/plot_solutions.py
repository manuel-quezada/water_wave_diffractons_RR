import numpy as np
from matplotlib import pyplot as plt

# Read data from Matlab files #
hom_data_for_python = np.genfromtxt('hom_data_for_python.csv',delimiter=',')
FV_data_for_python = np.genfromtxt('FV_data_for_python.csv',delimiter=',')

##################
# PLOT 1 at t=20 #
##################
x_hom = hom_data_for_python[:,0]
x_FV = FV_data_for_python[:,0]
eta_hom = hom_data_for_python[:,1]
eta1_FV = FV_data_for_python[:,1]
eta2_FV = FV_data_for_python[:,2]

DXLeft=25; DXRight=15
xmax=x_hom[np.argmax(eta_hom)]
shift=-100

plt.figure(figsize=(40,6.5))
plt.subplot(131)
plt.plot(x_hom+shift,eta_hom,'-k',linewidth=4)
plt.plot(x_FV,eta1_FV,'--b',linewidth=5)
plt.plot(x_FV,eta2_FV,'-r',linewidth=4)
plt.ylim([0.75-0.0002, 0.7506])
plt.xlim([xmax+shift-DXLeft,xmax+shift+DXRight])
plt.gca().ticklabel_format(useOffset=False)
plt.yticks([0.7498,0.75,0.7502,0.7504,0.7506])
plt.tick_params(labelsize=30)
plt.gca().yaxis.offsetText.set_fontsize(20)

###################
# PLOT 3 at t=120 #
###################
eta_hom = hom_data_for_python[:,2]
eta1_FV = FV_data_for_python[:,3]
eta2_FV = FV_data_for_python[:,4]

xmax=x_hom[np.argmax(eta_hom)]
shift=100
shift_FV=200

plt.subplot(132)
plt.plot(x_hom+shift,eta_hom,'-k',linewidth=4)
plt.plot(x_FV+shift_FV,eta1_FV,'--b',linewidth=5)
plt.plot(x_FV+shift_FV,eta2_FV,'-r',linewidth=4)
plt.ylim([0.75-0.0002, 0.7506])
plt.xlim([xmax+shift-DXLeft,xmax+shift+DXRight])
plt.tick_params(labelsize=30)
plt.gca().axes.get_yaxis().set_visible(False)

###################
# PLOT 4 at t=200 #
###################
eta_hom = hom_data_for_python[:,3]
eta1_FV = FV_data_for_python[:,5]
eta2_FV = FV_data_for_python[:,6]

xmax=x_hom[np.argmax(eta_hom)]
shift=300
shift_FV=400

plt.subplot(133)
line1=plt.plot(x_hom+shift,eta_hom,'-k',linewidth=4)[0]
line2=plt.plot(x_FV+shift_FV,eta1_FV,'--b',linewidth=5)[0]
line3=plt.plot(x_FV+shift_FV,eta2_FV,'-r',linewidth=4)[0]
plt.ylim([0.75-0.0002, 0.7506])
plt.xlim([xmax+shift-DXLeft,xmax+shift+DXRight])
plt.tick_params(labelsize=30)
plt.gca().axes.get_yaxis().set_visible(False)

plt.figlegend(handles=(line1, line2, line3),
              labels=('Homogenized linear system',
                      'Shallow water model at y=0.25',
                      'Shallow water model at y=-0.25'),
              loc='upper center', ncol=3, labelspacing=20.,
              fontsize=30)
plt.savefig('homog_corr1.png',bbox_inches="tight")
