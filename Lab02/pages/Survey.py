# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).
import csv

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Data Collection Survey 📝")
st.write("Please fill out the form below answering the following question to add your data to the dataset:How Many Dogs Are on Different College Campuses?")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    categoryInput = st.text_input("Enter a category:")
    valueInput = st.text_input("Enter a corresponding value:")

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        # --- YOUR LOGIC GOES HERE ---
        # TO DO:
        # 1. Create a new row of data from 'category_input' and 'value_input'.
        # 2. Append this new row to the 'data.csv' file.
        #    - You can use pandas or Python's built-in 'csv' module.
        #    - Make sure to open the file in 'append' mode ('a').
        #    - Don't forget to add a newline character '\n' at the end.
        data=[{categoryInput}, {valueInput}]
        if not os.path.exists('data.csv') or os.path.getsize('data.csv') == 0:
            headerNames=["College Campus", "Number of Dogs Seen"]
            with open("data.csv", "a", newline="") as file: #A IS APPEND, W IS WRITING, R IS READ. BEFORE SUBMITTING, WE CHANGE THIS BACK TO A
                writer= csv.writer(file)
                writer.writerow(headerNames)
                writer.writerow(data)
            st.success("Your data has been submitted!")
            st.write(f"You entered: **Category:** {categoryInput}, **Value:** {valueInput}")
        else:
            with open("data.csv", "a", newline="") as file: #A IS APPEND, W IS WRITING, R IS READ. BEFORE SUBMITTING, WE CHANGE THIS BACK TO A
                writer= csv.writer(file)
                writer.writerow(data)
            st.success("Your data has been submitted!")
            st.write(f"You entered: **Category:** {categoryInput}, **Value:** {valueInput}")
        


# DATA DISPLAY #Number of dogs seen on different college campuses 
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV","w")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")

