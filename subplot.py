import pandas as pd
import matplotlib.pyplot as plt

import os
os.chdir('D:/Python')

##read data
data1=pd.read_csv('picturel.csv')
data2=pd.read_csv('picturej.csv')
data3=pd.read_csv('pictureh.csv')
data4=pd.read_csv('pictureq.csv')

##set index
index2=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
index1=['2001','2003','2005','2007','2009','2011','2013','2015']

data1.index=index2
data2.index=index2
data3.index=index2
data4.index=index2

fig=plt.figure()

ax1=fig.add_subplot(2,2,1)
plt.plot(data1)
ax1.set_xticks(list(range(0,15,2)))   ## location of xticks
ax1.set_xticklabels(index1,fontsize=10)
plt.ylim([0.3,0.8])              ##
ax1.set_title('Coupling Coordinated Degree of Liao',fontsize=12)

ax2=fig.add_subplot(2,2,2)
plt.plot(data2)         ##
ax2.set_xticks(list(range(0,15,2)))   ## location of xticks
ax2.set_xticklabels(index1,fontsize=10)
plt.ylim([0.3,0.8])              ##
ax2.set_title('Coupling Coordinated Degree of Ji',fontsize=12)

ax3=fig.add_subplot(2,2,3)
plt.plot(data3)         ##
ax3.set_xticks(list(range(0,15,2)))   ## location of xticks
ax3.set_xticklabels(index1,fontsize=10)
plt.ylim([0.3,0.8])              ##
ax3.set_title('Coupling Coordinated Degree of Hei',fontsize=12)

ax4=fig.add_subplot(2,2,4)
plt.plot(data4)         ##
ax4.set_xticks(list(range(0,15,2)))  ## location of xticks
ax4.set_xticklabels(index1,fontsize=10)
plt.ylim([0.3,0.8])              ##
ax4.set_title('Nationwide Coupling Coordinated Degree',fontsize=12)

plt.subplots_adjust(hspace=0.2,wspace=0.2)
plt.show()