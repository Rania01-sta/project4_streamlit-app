import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Class Demo",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Live Demo of the Streamlit App")
st.write(""""
Welcome to this demo project! This streamlit app is designed to be a step-by-step tutorial for beginners. In this project, we will cover several key components:
- Creating titles and headers
- Using sidebars for navigation and gathering user inputs
- Displaying text, markdown and data tables
- Generating data with Numpy and Pandas.
- Visualizing data with charts.
- **Interactive** widgets like buttons and sliders.

*Each section of the code is connected extensively to help you understand its purpose.*
""")

st.sidebar.header("User Input Features")
name = st.sidebar.text_input("Enter your name:", "Mary")

           
datapoints = st.sidebar.slider("Number of data points for chart:", min_value=5, max_value=100, value=30)

st.subheader(f"Hello, {name}! Let's create something interactive.")

dates = pd.date_range(start=pd.Timestamp.today(), periods=datapoints, freq="D")
random_data = np.random.randn(datapoints)

df = pd.DataFrame({
    "Date": dates,
    "Random Values": random_data 
})

df.set_index("Date", inplace=True)
st.write("Here is your generated data set:", df)

st.write("### Random Data Over Time")
st.line_chart(df)

if st.button("Generate New Random Data"):
    rndm_data = np.random.randn(datapoints)
    df["Random Values"] = rndm_data

    st.write("### New Random Data Chart Over Time")
    st.line_chart(df)
    st.info("New Random Data Generated!")

st.write("""
- **Page Configuration:** Sets up the app's title and layout.
- **Introduction:** Explains the purpose and guides you through the project.
- **Sidebar Widgets:** Collect user inputs (name and number of data points) in a non-intrusive manner.   
- **Data Generation:** Demonstrates how to create and manipulate data with pandas and Numpy.
- **Data Visualization:** Uses a line chart to visualize data trends.
- **Interactivity:** Introduces a button widget that lets users refresh the data.
         
        1.  This modular approach can be expanded witha additional features like more charts, additional widgets, or even connecting to real-world APIs for dynamic data.
        2.  The app is designed to be user-friendly and educational, making it a great starting point for anyone looking to learn about Streamlit and data visualization.
         
### Next Steps
- Explore the Streamlit documentation for more widgets and features.
""")

st.write("### Additional Resources")
st.write("""
- [Streamlit Documentation](https://docs.streamlit.io/)
""")
