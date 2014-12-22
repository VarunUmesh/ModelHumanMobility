import pandas as pd
import numpy as np

# Read the home location csv file into the data frame

df = pd.read_csv('output_home_antenna.csv')
grp = df.groupby(['AntennaID']).agg({'UserID' : np.size})

# Rename the column name to home count

grp.reset_index(inplace=True)
grp.columns = ['AntennaID', 'Home_Count']


# Get the probability of the Home locations

grp['Probability_Of_Home_Location'] = grp['Home_Count'] / sum(grp['Home_Count'])

# Save the probabilities in a csv file

grp.to_csv('Probability_Of_Home_Location.csv', index=False)