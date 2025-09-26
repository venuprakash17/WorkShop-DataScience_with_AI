import streamlit as st
import pandas as pd
import numpy as np
import time

# Set the page configuration for a wider layout
st.set_page_config(layout="wide")

# --- Page Organization: Sidebar, Tabs, and Expander ---

# The sidebar is great for navigation or control widgets
st.sidebar.title("App Navigation & Controls")
page_option = st.sidebar.selectbox(
    "Choose a page to view:",
    ["Hello Streamlit 👋", "Data & Charts", "More Widgets"]
)

# An expander can be used to hide or show content
with st.sidebar.expander("About this app"):
    st.write(
        "This app demonstrates the core features of Streamlit, including widgets, data display, and layout organization.")

# Use tabs to organize content on the main page
tab1, tab2, tab3 = st.tabs(["👋 Basic", "📊 Data", "⚙️ Widgets"])

# --- Tab 1: Basic Structure ---
with tab1:
    st.title("Hello Streamlit 👋")
    st.write("This tab shows the most basic structure of a Streamlit app.")

    # Input widget
    name = st.text_input("Enter your name:")

    # Button & Output
    if st.button("Greet"):
        if name:
            st.success(f"Hello, {name}! This is a success message.")
        else:
            st.warning("Please enter your name first!")

# --- Tab 2: Data and Charts ---
with tab2:
    st.header("Displaying Data & Charts")
    st.write("Streamlit makes it easy to visualize data from pandas DataFrames.")

    # Create a sample DataFrame
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )

    # Display the DataFrame
    st.subheader("Data Table")
    st.dataframe(df)

    # Display a line chart
    st.subheader("Line Chart")
    st.line_chart(df)

    # Display a bar chart
    st.subheader("Bar Chart")
    st.bar_chart(df)

# --- Tab 3: Common Widgets and Outputs ---
with tab3:
    st.header("Common Widgets (Inputs) & Outputs")
    st.write("A collection of common input and output elements.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input Widgets")
        # Text input
        st.text_input("Text input:")

        # Numeric input
        st.number_input("Numeric input:", min_value=0, max_value=100)

        # Slider
        st.slider("Age:", 18, 100, 25)

        # Selectbox (dropdown)
        st.selectbox("Gender:", ["Male", "Female", "Other"])

        # Multiselect
        st.multiselect("Choose hobbies:", ["Music", "Sports", "Coding", "Reading", "Cooking"])

        # Checkbox
        accepted_terms = st.checkbox("Accept terms and conditions")

    with col2:
        st.subheader("Output Elements")
        # Displaying a progress bar
        st.write("This is a simple progress bar.")
        progress_bar = st.progress(0)
        for i in range(101):
            progress_bar.progress(i)
            time.sleep(0.01)

        # Displaying different types of messages
        st.success("This is a green success message.")
        st.warning("This is a yellow warning message.")
        st.error("This is a red error message.")

        # Displaying a JSON object
        st.write("This is a JSON display:")
        st.json({"key": "value", "list_of_numbers": [1, 2, 3]})

# --- Final Expander for an explanation at the bottom ---
with st.expander("See the code structure explanation"):
    st.markdown("""
    This app is organized to demonstrate Streamlit's key features:
    - **Imports:** We import `streamlit`, `pandas`, `numpy`, and `time`.
    - **Page Configuration:** `st.set_page_config` is used to adjust the app's initial layout.
    - **Layout:** The app is structured using `st.sidebar` for controls and `st.tabs` for different sections of content.
    - **Widgets:** We use various input widgets like `text_input`, `slider`, and `multiselect` to collect user data.
    - **Outputs:** We use `st.success`, `st.warning`, `st.error`, and `st.progress` to provide feedback.
    - **Data:** `pandas` and `numpy` are used to create sample data, which is then displayed with `st.dataframe` and various chart functions.
    """)
