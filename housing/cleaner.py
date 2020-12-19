import pandas as pd
import numpy as np

house = pd.read_csv('xinyi_scraped.csv')

"""TO DO LIST:

1. Drop useless column(s)

2. Parse data
   - Get region from 'Address' into separate dataframe [x]
   - Remove Chinese characters from 'Age', 'Area1', 'Area2'
   - Rename 'Area1', 'Area2'
   - Parse out number of rooms from 'Rooms' and put number of each type of rooms into separate columns [x]
   - 'FloorNum' - Remove weird 2nd half part from 'FloorNum' features [x]
   - Get number of unique tag values in 'Tag'; then separate for each tag separate into different columns with boolean (0 for tag isn't present, 1 for tag is present)
   - Convert 'Price' to float. [x]

3. Create new csv to be processed for EDA.

"""

# Dropped useless column
house = house.drop(['Unnamed: 0'], axis=1)

#------ Parse out region from 'Address' ------#
house['Region'] = house['Address'].str.slice(3, 6)

#------ Remove chinese character from 'Age' and convert column to 'float64' ------#
# print(house['Age'].unique())
house['Age'] = house['Age'].replace('預售', np.NaN).replace('--', np.NaN)
house['Age'] = house['Age'].str.replace('年', '')
house['Age'] = house['Age'].astype('float64')

# ------ Remove chinese character from 'Area1' and convert column to 'float64' ------# - Come back later, a bit complicated
# print(house['Area1'].unique())

#------ Parse out num rooms and put in separate columns ------#
rooms = house['Rooms'].str.extract(
    r'([0-9]房)?([0-9]廳)?(([0-9])?(.[0-9])?衛)?([0-9]室)?')
rooms = rooms.drop(columns=[3, 4])
rooms = rooms.rename(
    columns={0: 'Bedrooms', 1: 'Living rooms', 2: 'Bathrooms', 5: 'Shi'})
house['Bedroom'] = rooms['Bedrooms'].str.slice(stop=1)
house['Bedroom'] = house['Bedroom'].replace(np.NaN, 0).astype('int')

house['Bathroom'] = rooms['Bathrooms'].str.slice(stop=1)
house['Bathroom'] = house['Bathroom'].replace(np.NaN, 0).astype('int')

house['LivingRooms'] = rooms['Living rooms'].str.slice(stop=1)
house['LivingRooms'] = house['LivingRooms'].replace(np.NaN, 0).astype('int')

house['HeShi'] = rooms['Shi'].str.slice(stop=1)
house['HeShi'] = house['HeShi'].replace(np.NaN, 0).astype('int')
# print(house['Bedroom'].unique())
# print(house[house.Bedroom == 9])


#------ Convert price to float ------#
house['Price'] = house['Price'].str.replace(',', '').astype('float64')
# print(house['Price'].unique())

#------ Remove weird 2nd half part from 'FloorNum' features ------#
house['FloorNum'] = house['FloorNum'].str.split('/').str[0]
house['FloorNum'] = house['FloorNum'].str.replace('樓', '')
house['FloorNum'] = house['FloorNum'].str.replace('~', '-')
house['FloorNum'] = house['FloorNum'].str.split('-').str[0]
house['FloorNum'] = house['FloorNum'].replace('', np.nan)
house['FloorNum'] = house['FloorNum'].str.split(',').str[0]
house['FloorNum'] = house['FloorNum'].str.split('、').str[0]
house['FloorNum'] = house['FloorNum'].replace(
    'B1', '1').replace('B2', '2').replace('B3', '3')
house['FloorNum'] = house['FloorNum'].replace(np.nan, 0).astype('int')
# print(house)


#------ Get number of unique tag values in 'Tag' ------#
# print(house['Tags'].unique())
attributes = []
for tag in house['Tags']:
    one_row = tag.replace('[', '').replace(']', '')
    one_row = one_row.replace('\'', '')
    one_row = one_row.split(', ')
    for j in one_row:
        if j not in attributes:
            attributes.append(j)
print(attributes)
for tag in house['Tags']:
    one_row = tag.replace('[', '').replace(']', '')
    one_row = one_row.replace('\'', '')
    one_row = one_row.split(', ')


# print(house.columns)
# print()
# print(house.dtypes)
# print()
# print(house.head())
