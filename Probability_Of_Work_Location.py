import pandas as pd
import numpy as np

# Read the home location csv file into the data frame

df = pd.read_csv('output_work_antenna.csv')
grp = df.groupby(['AntennaID']).agg({'UserID' : np.size})

# Rename the column name to home count

grp.reset_index(inplace=True)
grp.columns = ['AntennaID', 'Work_Count']

# Get the probability of the Home locations

grp['Probability_Of_Work_Location'] = grp['Work_Count'] / sum(grp['Work_Count'])

# Save the probabilities in a csv file

grp.to_csv('Probability_Of_Work_Location.csv', index=False)