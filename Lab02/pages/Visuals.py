# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")


import streamlit as st
import pandas as pd
import json
import os

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.

df_json = pd.DataFrame()
try:
    df_csv = pd.read_csv("data.csv")
    st.success("CSV data loaded successfully!")
    st.write("CSV Data Preview:")
    st.write(df_csv.head())
except Exception as e:
    st.error(f"Error loading CSV: {e}")
    df_csv = pd.DataFrame()

try:
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            my_dict = json.load(file)
            df_json = pd.DataFrame(my_dict["data_points"])
            st.success("JSON data loaded successfully!")
    else:
        st.warning("data.json not found.")
except Exception as e:
    st.error(f"An unexpected error occurred while loading JSON: {e}")

# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Graph 1: Static") 
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.
st.line_chart(df_json, x="Year", y=df_json.columns.drop("Year"))
st.write("Description: The carbon emissions steadily increase from 2018-2020, then unevenly drop.")


# GRAPH 2: DYNAMIC GRAPH 
st.subheader("Graph 2: Total Greenhouse Gas Emissions of Gambia in Megatons") 
# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.


st.write("JSON columns:", df_json.columns.tolist() if not df_json.empty else "No JSON data")
if not df_json.empty and "Year" in df_json.columns and "Total Emissions" in df_json.columns:
   
    df_to_use = df_json[["Year", "Total Emissions"]]
    st.info("Using JSON data for Graph 2 (Year and Total Emissions only)")
else:
    st.error("JSON data doesn't have the required columns (Year, Total Emissions)")
    st.write("Available columns:", df_json.columns.tolist() if not df_json.empty else "No data")
    df_to_use = pd.DataFrame()

if not df_to_use.empty:

    if "selected_year" not in st.session_state:
        st.session_state.selected_year = df_to_use["Year"].iloc[0]  #NEW
    
    
    selected_year = st.selectbox("Select a year:",  #NEW
                                df_to_use["Year"].unique(),
                                index=0,
                                key="selected_year"
    )
    
    new_df = df_to_use[df_to_use["Year"] == selected_year]
    
    st.line_chart(new_df, x="Year", y="Total Emissions")  #NEW
    
    st.write("Description: This graph shows greenhouse gas emissions for the selected year. Use the dropdown to select different years and see how emissions change over time.")


# GRAPH 3: DYNAMIC GRAPH
st.subheader("Graph 3: Number of Dogs on Different College Campuses?") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.
selected_college= None
if not df_csv.empty:
    if "selected_college" not in st.session_state:
        st.session_state.selected_college = df_csv["College Campus"].iloc[0] #new 
    selected_college= st.selectbox("Select a College Campus:", #new 
                            df_csv["College Campus"].unique(),
                               key="selected_college"
    )
                            
    new_df_csv= df_csv[df_csv["College Campus"]== selected_college]
    st.bar_chart(new_df_csv,x="College Campus", y="Number of Dogs Seen")
    st.write("Description:This graph shows the number of dogs at different colleges.")

