import pandas as pd
import plotly.express as px
import streamlit as st

# Loading the CSV
df = pd.read_csv('vehicles_us.csv')

# Fixing the data
# ---------------

# Filtering rows with invalid data
for col in ['model_year', 'odometer']:
    df = df[df[col].notnull()]

# Setting 'unknown' for unknown paint_color values
df['paint_color'] = df['paint_color'].fillna('unknown')

# Converting the is_4wd from 1.0/NA to boolean
df['is_4wd'] = df['is_4wd'].fillna(0)
df['is_4wd'] = df['is_4wd'] == 1

# Adding the manufacturer column. Assuiming the first word of the model is that.
df['manufacturer'] = df['model'].str.split(' ').str[0]

# Writing the App's header
st.header("DL Development Tools Project App")

# Create a checkbox for filtering the year
filter_year = st.checkbox('Filter by Year')

if filter_year:
    # Allow user to select a year
    selected_year = st.selectbox('Select Year', df['model_year'].unique())

    # Filter the data based on the selected year
    df_filtered = df[df['model_year'] == selected_year]
else:
    # If checkbox is not selected, show all data
    df_filtered = df.copy()

# Group the filtered DataFrame by 'manufacturer', 'model_year', and 'is_4wd', and then count the number of 4WD cars per year per model
df_count = df_filtered[df_filtered['is_4wd']].groupby(['manufacturer', 'model_year']).size().reset_index(name='count')

# Create a bar chart using Plotly Express
fig = px.bar(df_count, x='model_year', y='count', color='manufacturer', barmode='group', title='Amount of 4WD Cars per Year per Manufacturer')

# Writing the histogram to the app
st.write(fig) 




