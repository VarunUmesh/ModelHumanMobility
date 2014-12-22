# -*- coding: utf-8 -*-
"""
Identying user's work and home tower.
"""

def classify_weekday(data):
    if ( data.weekday() == 5 ):
        return 'Weekend'
    elif ( data.weekday() == 6 ):
        return 'Weekend'
    else:
        return 'Weekday'

def classify_hour(data):
    if 4 < int(data) < 6:
        return 'A' # 04:00-06:00'
    elif 6 <= int(data) < 7:
        return 'B1' # 06:00-07:00'
    elif 7 <= int(data) < 8:
        return 'B2' # 07:00-08:00'
    elif 8 <= int(data) < 9:
        return 'B3' # 08:00-09:00'
    elif 9 <= int(data) < 10:
        return 'B4' # 09:00-10:00'
    elif 10 <= int(data) < 12:
        return 'C1' # 10:00-12:00'
    elif 12 <= int(data) < 14:
        return 'D' # 12:00-14:00'
    elif 14 <= int(data) < 16:
        return 'C2' # 14:00-16:00'
    elif 16 <= int(data) < 18:
        return 'E1' # 16:00-18:00'
    elif 18 <= int(data) < 21:
        return 'E2' # 18:00-21:00'
    elif 21 <= int(data) < 24:
        return 'F1' # 21:00-24:00'
    elif 0 <= int(data) < 4:
        return 'F2' # 00:00-04:00'
    else:
        return '-'

from pandas import pandas as pd
# from datetime import datetime as dt
# from random import random as rand
# from numpy.random import randn

print '1/8 - Loading data'
df = pd.read_csv('dataset.csv',
                 header=None,
                 parse_dates=[1],
                names=['UserID', 'DateTime', 'AntennaID'],
                infer_datetime_format=True)

temp = pd.DatetimeIndex(df['DateTime'])
df['Date'] = temp.date
df['Time'] = temp.time

"""
# Filtering User
df_user_1 = df.groupby(['UserID'], sort=False).agg({"Date": lambda x: x.nunique()})
df_user_2 = df_user_1[df_user_1['Date'] > 2]
df_user_3 = df_user_2['Date']
df_user_3.to_csv('output_df_user.csv')
df_user_list = pd.read_csv('output_df_user.csv',
                 header=None,
                names=['UserID', 'DaySeen'])
df['ActiveUser'] = df['UserID'].isin(df_user_list['UserID'])
"""

df['DayData'] = df['DateTime'].apply(classify_weekday)
df['HourData'] = df['DateTime'].apply(lambda x: x.hour)
df['Bin'] = df['HourData'].apply(classify_hour)

df_active = df[df['AntennaID'] != -1 ]
df_weekday = df_active[df_active['DayData'] == 'Weekday']

print '2/8 - Grouping by UserID, Bin, AntennaID'
# Step 1: UserID - Bin - AntennaID - Date - Count
# Step 2: UserID - Bin - AntennaID - Count
by_usr_bin_1 = df_weekday.groupby(['UserID', 'Bin', 'AntennaID'], sort=False)
by_usr_bin_2 = by_usr_bin_1.size().reset_index()
# by_usr_bin_3 = by_usr_bin_2.groupby(['UserID', 'Bin'], sort=False).first()

print '3/8 - For Work Antenna: Filtering for only C1 Bin'
by_usr_bin_work = by_usr_bin_2.groupby(['UserID', 'Bin'], sort=False).filter(lambda x:x.Bin=='C1')
print '4/8 - For Work Antenna: Selecting Top Antenna'
by_usr_bin_work_final = by_usr_bin_work.groupby(['UserID'], sort=False).first()
print '5/8 - For Work Antenna: Exporting for Work'
by_usr_bin_work_final.to_csv('output_work_antenna.csv')

print '6/8 - For Home Antenna: Filtering for only F1 Bin'
by_usr_bin_home = by_usr_bin_2.groupby(['UserID', 'Bin'], sort=False).filter(lambda x:x.Bin=='F1')
print '7/8 - For Home Antenna: Selecting Top Antenna'
by_usr_bin_home_final = by_usr_bin_home.groupby(['UserID'], sort=False).first()
print '8/8 - For Home Antenna: Exporting for Home'
by_usr_bin_home_final.to_csv('output_home_antenna.csv')
