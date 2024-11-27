import pandas as pd

# Read the original CSV file
df = pd.read_csv('CORSFINAL2.csv')

# Sort the data by 'state_name'
sorted_df = df.sort_values(by='state_name')

# Save the sorted data to a new CSV file
sorted_df.to_csv('sorted_by_state.csv', index=False)