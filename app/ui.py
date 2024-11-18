import streamlit as st
import pandas as pd

# Import functions from the backend
from backend.data_preprocessing import combine_data
from backend.model import lstm_predict
from backend.allocation import allocate_resources


def run_app():
    st.title("Dasma Resource Allocation Prediction")

    # Generate mock combined data
    data = combine_data()

    # Show the combined data in the Streamlit app
    st.write("Combined Data:")
    st.write(data)

    # Button to run prediction and allocation
    if st.button("Predict and Allocate Resources"):
        predictions = lstm_predict(data)
        allocations = allocate_resources(predictions)
        st.write("Predictions:", predictions)
        st.write("Resource Allocations:", allocations)
