import pandas as pd

from constants import INVERT
from utils import selected_variables, country_codes, inverted_variables

# Read the CSV file
data = pd.read_csv('resources/dataset/WVS_Cross-National_Wave_7_csv_v5_0.csv', low_memory=False)

# Discard variables not in the selected_variables dictionary
data = data[selected_variables.keys()]

# Rename the selected variables
data = data.rename(columns=selected_variables)

# Convert country codes to full names
data['country'] = data['country'].map(country_codes)

# Invert column values, so we keep the same pattern
if INVERT:
    for variable, min_, max_ in inverted_variables:
        positive_values = data[variable] > 0
        data.loc[positive_values, variable] = max_ + min_ - data.loc[positive_values, variable]

# Write the new CSV file
new_file_name = 'WVS_Cross-National_Wave_7_csv_v5_0_social_religious_ethical.csv'
data.to_csv(new_file_name, index=False)
