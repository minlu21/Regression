import pandas as pd
import numpy as np

auto = pd.read_csv('auto.data')
auto.columns = ['Symboling', 'NormLosses', 'Make', 'Fuel-Type', 'Aspiration', 'NumDoors', 'Body-Style',
                'Drive-Wheels', 'EngineLoc', 'WheelBase', 'Length', 'Width', 'Height', 'CurbWeight', 'EngineType', 'NumCylinders', 'EngineSize', 'FuelSys', 'Bore', 'Stroke', 'CompressRatio', 'HorsePower', 'PeakRPM', 'CityMPG', 'HighwayMPG', 'Price']

# Replace missing data with np.nan [x]
# Check for validity of data in every column. [x]
# Convert to correct datatypes [x]

auto = auto.replace('?', np.nan)

# Converted to correct datatypes
auto['NormLosses'] = auto['NormLosses'].astype('float64')

door_num_map = {'two': 2, 'four': 4}
auto['NumDoors'] = auto['NumDoors'].map(door_num_map)

cylinder_num_map = {'four': 4, 'six': 6, 'five': 5,
                    'three': 3, 'twelve': 12, 'two': 2, 'eight': 8}
auto['NumCylinders'] = auto['NumCylinders'].map(cylinder_num_map)

auto['Bore'] = auto['Bore'].astype('float64')
auto['Stroke'] = auto['Stroke'].astype('float64')
auto['HorsePower'] = auto['HorsePower'].astype('float64')
auto['PeakRPM'] = auto['PeakRPM'].astype('float64')
auto['Price'] = auto['Price'].astype('float64')

# print(auto.info())

# Impute categorical data with mode of column, continuous data with mean of column
for column in auto.columns:
    if auto[column].dtype == 'object':
        auto[column] = auto[column].fillna(auto[column].mode())
    if auto[column].dtype == 'float64':
        auto[column] = auto[column].fillna(round(auto[column].mean(), 2))
    if auto[column].dtype == 'int':
        auto[column] = auto[column].fillna(auto[column].mode())
    print(auto[column].unique())
    print()

# Encoding nominal features - 'Make', 'Fuel-Type', 'Aspiration',
