import pandas as pd
import numpy as np

# Replace empty entries with Nones
df_pin = df_pin.fillna(value=None)

# Replace non-numeric entries in follower_count with Nones
df_pin['follower_count'] = pd.to_numeric(df_pin['follower_count'], errors='coerce')

# Convert follower_count to integer dtype
df_pin['follower_count'] = df_pin['follower_count'].astype('Int64')

# Set numeric columns to numeric dtypes
numeric_cols = ['follower_count']
df_pin[numeric_cols] = df_pin[numeric_cols].apply(pd.to_numeric)

# Clean save_location column
df_pin['save_location'] = df_pin['save_location'].str.extract(r'(.*)\?')

# Rename index to ind
df_pin.rename(columns={'index':'ind'}, inplace=True)

# Reorder columns
df_pin = df_pin[['ind', 'unique_id', 'title', 'description', 'follower_count', 
                 'poster_name', 'tag_list', 'is_image_or_video', 'image_src',
                 'save_location', 'category']]
