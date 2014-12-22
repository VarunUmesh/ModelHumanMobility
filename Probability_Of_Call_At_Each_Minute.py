import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import os
from scipy.stats import norm
from scipy import stats
from scipy.stats.kde import gaussian_kde
from matplotlib.collections import LineCollection
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec
import matplotlib.mlab as mlab
import linecache
import csv
import sys
import traceback
#import seaborn as sns
from scipy.spatial import Voronoi, Delaunay
from ast import literal_eval

'''
df = pd.read_csv("all_files.csv", parse_dates=[1])
df['Hour'] = df['DateTime'].apply(lambda x: x.hour)
grp = df.groupby(['UserID', 'Hour']).agg({'AntennaID' : {'count':np.size}})
grp.reset_index(level=0, inplace=True)
grp.reset_index(level=0, inplace=True)
grp.head()
grp.columns = ['Hour', 'UserID', 'Count']

plt.close('all')
plt.scatter(grp['Hour'], grp['Count'], marker='.', s=.5, color='b')
plt.yscale('log')
plt.title('ML PLOT 1')
#plt.xlim(.1, max(f['CALLS_AVG']))
#plt.ylim(0, 120)
#plt.show()
plt.savefig('ml-plot-1.png')
'''

grp = pd.read_csv('ml_int_p1.csv')

def set_class_name(count):
    if 6 <= count <= 13:
        return 'A'
    elif 16 <= count <= 23:
        return 'B'
    else:
        return 'C'
        
grp['Class'] = grp['Hour'].apply(lambda x: set_class_name(x))
gr = grp[grp['Class'] != 'C']

dfgr = gr.groupby(['UserID', 'Class']).agg({'Count': np.sum})
hh = dfgr.unstack()
hh.reset_index(level=0, inplace=True)
hh.columns = ['UserID', 'A', 'B']

def setclass(data):
    if data['A'] >= data['B']:
        return 'A'
    else:
        return 'B'

hh['Class'] = hh.apply(lambda x: setclass(x), axis = 1)
del grp['Class']
grp = pd.merge(grp, hh, on='UserID', how='outer')

clb = grp[grp['Class'] == 'B'].groupby('Hour').agg({'Count' : np.mean})
clb.reset_index(level=0, inplace=True)
clb.columns = ['Hour', 'Avg_Count']

cla = grp[grp['Class'] == 'A'].groupby('Hour').agg({'Count' : np.mean})
cla.reset_index(level=0, inplace=True)
cla.columns = ['Hour', 'Avg_Count']

clc = grp[grp['Class'] == 'C'].groupby('Hour').agg({'Count' : np.mean})
clc.reset_index(level=0, inplace=True)
clc.columns = ['Hour', 'Avg_Count']


plt.close('all')
plt.plot(cla['Hour'], cla['Avg_Count'], 'r-', label='A')
plt.plot(clb['Hour'], clb['Avg_Count'], 'b-', label='B')
plt.xlim(0, 23)
plt.legend(loc='best')
plt.title('ML PLOT 3')
plt.savefig('ml-plot-3.png')