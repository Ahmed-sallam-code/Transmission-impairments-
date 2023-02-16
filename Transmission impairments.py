import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from math import sin
from math import pi
from math import cos 
import random
y=[]
s=[]
s1=[]
s2=[]
s3=[]
xpoints=np.array(np.arange(-2*pi, 2*pi, 0.0001))
randomlist = []
for i in range(0,len(xpoints)):
    n = random.randint(-100,100)
    randomlist.append(n/100)
randomlist=np.array(randomlist)
for i in range(len(xpoints)):
    s1+=[0.2*cos(5*pi*xpoints[i])]  
    s2+=[0.2*sin(10*pi*xpoints[i]-(pi))]
    s3+=[0.2*cos(15*pi*xpoints[i]-(pi/6))]
ypoints=np.array(y)
s1points=np.array(s1)
s2points=np.array(s2)
s3points=np.array(s3)
#plt.plot(xpoints,s1points,'--',alpha=0.5)
#plt.plot(xpoints,s2points,'--',alpha=0.5)
#plt.plot(xpoints,s3points,'--',alpha=0.5)
#plt.plot(xpoints,randomlist) 
plt.plot(xpoints,s1points+s2points+s3points+randomlist,"hotpink")
plt.ylabel("Voltage")
plt.xlabel("Time")
plt.xlim(0,0.5)
plt.grid()
plt.show()   
#plt.subplot(2,1,1)
#plt.title("Transmitted Signal")
#plt.plot(xpoints,ypoints)
#plt.grid()
#plt.ylabel("Voltage")
#for i in range(len(xpoints)):
    #s+=[0.67*(sin(xpoints[i])*cos(3*pi*xpoints[i]))]
#ypoints1=np.array(s)   
#plt.subplot(3,1,2)
#plt.title("Recived Signal")
#plt.plot(xpoints,ypoints1,color="hotpink") 
#plt.ylabel("Voltage")
#plt.xlabel("Time")
#from numpy.fft import fft, ifft

#X = fft(ypoints)
#N = len(X)     
#n = np.arange(N)
#T = N*0.0001
#freq = n/T 


#plt.subplot(2,1,1)

#plt.stem(freq, np.abs(X), 'g', \
#         markerfmt=" ", basefmt="-g")
#plt.xlabel('Freq (Hz)')
#plt.ylabel('FFT Amplitude |X(freq)|')
#plt.xlim(0, 10)

#plt.subplot(2,1,2)
#plt.plot(xpoints, ifft(X), 'hotpink')
#plt.xlabel('Time (s)')
#plt.ylabel('Amplitude')
#plt.tight_layout()
#plt.show()