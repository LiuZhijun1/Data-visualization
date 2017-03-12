import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import os
os.chdir('D:/Python')

##read data
data1=pd.read_csv('picture5.csv')
##set index
index1=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
data1.index=index1

##draw picture
data1.plot(marker='o')


##set label
plt.xlabel('Year')
plt.ylabel('Coupling Coordinated Degree')
plt.ylim([0.35,0.7])
plt.legend(fontsize=13,loc='best')
