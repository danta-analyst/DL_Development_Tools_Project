import pandas as pd
import plotly.express as px
import streamlit as st

# Loading the CSV
df = pd.read_csv('vehicles_us_fixed.csv')

# Writing the App's header
st.header("DL Development Tools Project App")

# Create a checkbox for filtering the year
filter_year = st.checkbox('Filter by Year')

if filter_year:
    # Allow user to select a year
    selected_year = st.selectbox('Select Year', sorted(df['model_year'].unique(), reverse = True))

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

# Generating scatter plot for price Vs model year
# -----------------------------------------------

# filterring irelevant prices
df_filtered = df[df['price'] >= 100]
fig = px.scatter(df_filtered, x='model_year', y='price', 
                 hover_name='model', title='Price vs Model Year',
                 labels={'model_year': 'Model Year', 'price': 'Price'})

# Update layout
fig.update_layout(showlegend=False)

# Writing the histogram to the app
st.write(fig) 



