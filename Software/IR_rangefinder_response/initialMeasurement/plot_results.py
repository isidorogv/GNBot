#!/usr/bin/python
# encoding: utf-8

from helper import *

from pylab import *

import numpy as np


# https://klassenresearch.orbs.com/Plotting+with+Python
from matplotlib import rc
# Make use of TeX﻿
rc('text',usetex=True)
# Change all fonts to 'Computer Modern'
rc('font',**{'family':'serif','serif':['Computer Modern']})

f, ax = subplots(1,figsize=(11,5))

data = loadFromFile("","distanceLog.p")

print(data)



distances = np.array(data['distances'])
measurementMin = np.array(data['measurementMin'])
measurementMax = np.array(data['measurementMax'])


measurementMin = mapVals(measurementMin,0.,1023.,0.,5.)
measurementMax = mapVals(measurementMax,0.,1023.,0.,5.)
measurementAvg = (measurementMin+measurementMax)/2

ax.plot(distances,measurementMax,'r')
ax.plot(distances,measurementAvg,'g')
ax.plot(distances,measurementMin,'b')

#ax.plot([0,200],[0.7,0.7],'k--')
ax.plot([10,10],[0,3.5],'k--',linewidth=1.5)
ax.plot([80,80],[0,3.5],'k--',linewidth=1.5)
ax.plot([40,40],[0,3.5],'k--',linewidth=1.5)


my_red = (1,0,0,0.3)

ax.arrow(10, 2.8, 5, 0, head_width=0.1, head_length=5, fc='k', ec='k')
ax.arrow(40, 2.8, -5, 0, head_width=0.1, head_length=5, fc='k', ec='k')
ax.text(40-21, 2.3, 'Maximum\nsensitivity', fontsize=16)



ax.arrow(80, 2.8, -5, 0, head_width=0.1, head_length=5, fc='k', ec='k')
ax.text(85-31, 2.5, 'Manuf. spec.', fontsize=16)


ax.text(10+2.5, 3.2, '$d=10cm$', fontsize=14)
ax.text(40+2.5, 3.2, '$d=40cm$', fontsize=14)
ax.text(80+2.5, 3.2, '$d=80cm$', fontsize=14)


ax.arrow(10, 0.9, -2.5, 0, head_width=0.05, head_length=2.5, fc=my_red, ec=my_red)
ax.arrow(80, 0.9, 10, 0, head_width=0.1, head_length=5, fc=my_red, ec=my_red)
ax.text(82, 0.6, 'Outside manuf. spec.', fontsize=16)


ax.add_patch(Rectangle((0,0),10,3.5,linewidth=0,facecolor=my_red))
#ax.add_patch(Rectangle((80,0),200,3.5,linewidth=0,facecolor=my_red))

# Fitting to exponential curve

#x1 = 9.
#y1 = float(measurementAvg[6])

x1 = 12.
y1 = float(measurementAvg[7])

#x2 = 21.
#y2 = float(measurementAvg[9])

x2 = 37.
y2 = float(measurementAvg[11])

#x2 = 86.
#y2 = float(measurementAvg[14])

#x2 = 114.
#y2 = float(measurementAvg[15])




#D = x1
#A = y1
#B = np.e
#C = 0.1

print x1, y1, x2, y2

K = x1*(y1-y2) / (1.-x1/x2)
C = y2-K/x2
fit = K*(1./distances)+C
print("K="+str(K))
print("C="+str(C))

#K = 14.6358265503
#C = -0.173084289376

#a = (np.log(K)-np.log(C+y3))/np.log(x3)
#K = (x1**a)*(y1-y2) / (1.-(x1**a)/(x2**a))
#C = y2-K/(x2**a)
#fit = K*(1./(distances**a))+C
#print a, K, C

#ax.plot(distances,fit)


#ax.plot(K/(measurementAvg-C),measurementAvg,"o")





ax.set_ylim([0,3.5])
ax.set_xlim([0,200])

ax.set_ylabel('Sensor output [V]', fontsize=16)
ax.set_xlabel('Actual distance $d$ from sensor to wall [cm]', fontsize=16)

ax.set_title('IR rangefinder response curve (I)', fontsize=18)


ax.legend(["$Maximum$","$Average$","$Minimum$"])#,"fit"])

tight_layout()

savefig("IR_sensor_response_curve.pdf")
savefig("IR_sensor_response_curve.png")

show()
exit()

f, ax = subplots(1)

ax.plot(distances,K/(measurementAvg-C),"r")
ax.plot(distances,distances,"b")


show()


