import streamlit as st
import pandas as pd
import os
st.title("Form Data to CSV")
with st.form("user_input_form"):
    st.write("Enter your answers:")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150)
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Submit")
csv_file_path = "user_answers.csv"
data = pd.DataFrame(columns=["Name", "Age", "Email"])
if os.path.exists(csv_file_path):
    data = pd.read_csv(csv_file_path)
if submit_button:
    new_row = {"Name": name, "Age": age, "Email": email}
    data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
    data.to_csv(csv_file_path, index=False)
    st.success("Answers submitted successfully!")
st.write("Current data:")
st.write(data)
st.download_button(
        label="Download CSV File",
        data=data.to_csv(index=False).encode("utf-8"),
        file_name="user_answers.csv",
        mime="text/csv",
    )
