#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

##
# plot for num of antennas
'''
df = pd.read_csv('num_of_towers.csv', dtype={'UserID' : str, 'Num_of_Antennas' : np.int32})

plt.figure()
plt.subplot(211)
sns.kdeplot(df['Num_of_Antennas'], cumulative=True, color='r')
plt.title('(CDF) # of towers a user connects')
plt.ylabel('P(x)')
plt.xlabel('Number of Towers')

plt.subplot(212)
sns.distplot(df['Num_of_Antennas'], hist=False, color='r')
plt.title('(PDF) # of towers a user connects')
plt.ylabel('P(x)')
plt.xlabel('Number of Towers')

plt.tight_layout(pad=1.4)
plt.savefig('num_of_towers_user_associates.png')
'''
##
# plot for num of days
'''
df = pd.read_csv('num_of_days.csv', dtype={'UserID' : str, 'Num_of_Days' : np.int32})

plt.figure()
plt.subplot(211)
sns.kdeplot(df['Num_of_Days'], cumulative=True, color='r')
plt.title('(CDF) # of days a user is seen')
plt.ylabel('P(x)')
plt.xlabel('Number of Days')

plt.subplot(212)
sns.distplot(df['Num_of_Days'], hist=False, color='r')
plt.title('(PDF) # of days a user is seen')
plt.ylabel('P(x)')
plt.xlabel('Number of Days')

plt.tight_layout(pad=1.4)
plt.savefig('num_days_user_seen.png')
'''
print 'Complete./'