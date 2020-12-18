import pandas as pd
import numpy as np

house = pd.read_csv('xinyi_scraped.csv')

"""TO DO LIST:

1. Drop useless column(s)

2. Parse data
   - Get region from 'Address' into separate dataframe
   - Remove Chinese characters from 'Age', 'Area1', 'Area2'
   - Rename 'Area1', 'Area2'
   - Parse out number of rooms from 'Rooms' and put number of each type of rooms into separate columns
   - 'FloorNum' - Remove weird 2nd half part from 'FloorNum' features
   - Get number of unique tag values in 'Tag'; then separate for each tag separate into different columns with boolean (0 for tag isn't present, 1 for tag is present)
   - Convert 'Price' to float.

3. Create new csv to be processed for EDA.
   
"""

house = house.drop(['Unnamed: 0'], axis=1)
