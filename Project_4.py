# Import neccessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

##############################################################################################################################################################################
# Page Configuration
# The page's title and layout is configured here
st.set_page_config(
    page_title="Project 4",
    layout="wide",
    initial_sidebar_state="expanded",
)

#############################################################################################################################################################################
# App Title and Introduction
# We introduce the App here by stating its purpose and functionality.
st.title('Screen Time Reduction through Notification Optimization: A Data-Driven Approach')
st.image(Image.open("Apps.png"))
st.write('Welcome to Project 4!')
st.markdown('#### Introduction')
st.write("""
        In the world of today, excessive screen time has become a growing concern, affecting productivity, mental well-being and physical health. With smartphones and other digital devices constantly demanding user's attention through notifications, managing screen time has become increasingly challenging. This project, "Screen Time Reduction Through Notification Optimization: A Data-Driven Approach", explores how intelligently managing notificaions can significantly decrease unnecessary screen engagement. By leveraging user interaction with data and behavioural patterns, the project aims to develop and test strategies that optimize the timing, frequency, and relevance of notifications. Through this data-driven methodology, the study seeks to promote healthier digital habits while maintaing user satisfaction and device utility. This streamlit app is designed to break down the process of the project in steps. In this project, we will cover several key components such as:
- Data Loading, Cleaning and Preparation
- Exploratory Data Analysis (EDA)
- Advanced Analysis and Visualization
- Summary (Reporting and Insights)

***Each section of the code is connected extensively to help you understand its purpose.***
""")

st.markdown('#### Scope of the Study')
st.write("""
- There are 5 social apps = Instagram, Facebook, X, Whatsapp, and LinkedIn
- There is 1 gaming app (“8 Ball Pool”)
- There is 1 browser (“Safari”), and
- There is 1 movie app ('Netflix')
""")

######################################################################################################################################################################################
# Data Loading, Cleaning and Preparation and
# Sidebar for User Inputs (Displays the users input on the sidebar)

st.subheader('Part 1: Data Loading, Cleaning and Preparation')
df = pd.read_csv('screentime_analysis.csv')
df.rename(columns={'Usage (minutes)': 'Usage_minutes'}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
st.sidebar.header('User Input Features')
num_rows = st.sidebar.slider(label= "Select number of rows to display", min_value=10, max_value=len(df), value=30)# default value
st.write(f"Showing top {num_rows} rows on the dataset:")
st.dataframe(df.head(num_rows))

# Sidebar text area for user comment
user_comment = st.sidebar.text_area(
    label='Leave your comment or feedback here:',)
placeholder='Type your thoughts...'
if user_comment.strip():
    st.markdown('Viewer Commented')
    st.write(user_comment)

#######################################################################################################################################################################################
# Exploratory Data Analysis (EDA)
# We find the average and sum of data here

st.subheader('Part 2: Exploratory Data Analysis (EDA)')
# Comparing the average times opened for all apps on the dataset
avg_times_opened = df.groupby('App')['Times Opened'].mean()
avg_times_opened.sort_values(ascending=False, inplace=True)
# reseting the column from Times Opened to Avg Times Opened
average = avg_times_opened.reset_index(name='Avg Times Opened')
st.write("**Comparing the average times opened for all apps on the dataset**", average)


# Total Usage_per_notification ratio for each app
grouped_apps = df.groupby('App').agg({'Usage_minutes': 'sum', 'Notifications': 'sum'})
# Comparing Usage_per_notification ratio for each app
Usage_per_notif_ratios = grouped_apps['Usage_minutes'] / grouped_apps['Notifications']
Usage_per_notif_ratios.sort_values(ascending=False, inplace=True)
grouped_apps['Usage_per_notification_ratios'] = Usage_per_notif_ratios
st.write('**The Usage per notification ratio for each app is:**', grouped_apps)

# Does a higher Times Opened always correlate with higher Usage_minutes
corr = df['Times Opened'].corr(df['Usage_minutes']).round(2)
st.write("**Correlation between Times Opened and Usage_minutes for all apps is:**", corr)

#############################################################################################################################################################################################
# Visualizing Data with Charts
# We analyze the data and display its result on a chart

st.subheader('Part 3: Advanced Analysis and Visualization')

# (1)
# Outliers in usage minutes for Netflix
# Create the dataframe
data = pd.DataFrame(df)
# Plot with matplotlib and seaborn
fig, ax = plt.subplots(figsize=(5, 3))
st.markdown('#### 1. Boxplot showing the Usage_minutes for Netflix')
sns.boxplot(x=df[df['App'] == 'Netflix']['Usage_minutes'], data=data, ax=ax)
ax.set_xlabel('Usage_minutes', fontsize=8)
st.pyplot(fig)

# (2)
# Daily trends in Usage minutes for Instagram and Whatsapp
# Filter data for Instagram and WhatsApp
instagram_data = df[df['App'] == 'Instagram']
whatsapp_data = df[df['App'] == 'WhatsApp']
# Group by Date and calculate mean Usage_minutes
instagram_daily = instagram_data.groupby('Date')['Usage_minutes'].mean().reset_index()
whatsapp_daily = whatsapp_data.groupby('Date')['Usage_minutes'].mean().reset_index()
# Plot line chart showing daily trends in usage minutes
fig, ax = plt.subplots(figsize=(10, 6))
st.markdown('#### 2. Line Chart Showing Daily Trends in Usage minutes for Instagram and Whatsapp')
ax.plot(instagram_daily['Date'], instagram_daily['Usage_minutes'], label='Instagram',data=data)
ax.plot(whatsapp_daily['Date'], whatsapp_daily['Usage_minutes'], label='WhatsApp',data=data)
ax.set_xlabel('Date', fontsize=15)
ax.set_ylabel('Usage_minutes', fontsize=15)
plt.legend()
st.pyplot(fig)

# (3)
# Average daily notification for each app
average = df.groupby('App')['Notifications'].mean().reset_index()
# Plot bar chart
fig, ax = plt.subplots(figsize=(10,6))
st.markdown('#### 3. Average Daily Notifications Across All Apps')
ax.bar(average['App'], average['Notifications'], color = ['blue','yellow','green','orange','brown','grey','red','purple'])
ax.set_xlabel('App', fontsize=15)
ax.set_ylabel('Average Notifications', fontsize=15)
st.pyplot(fig)

# (4)
# Scatterplot exploring the relationship between Notifications and Times Opened for Facebook
#Flitter App
df_scatter = df[df['App'] == 'Facebook']
#Plot Graph
fig, ax = plt.subplots()
st.markdown('#### 4. Scatterplot exploring the relationship between Notifications and Times Opened for Facebook')
sns.regplot(x=df_scatter['Notifications'], y=df_scatter['Usage_minutes'], color='red', ax=ax)
ax.set_xlabel('Notifications')
ax.set_ylabel('Usage_minutes')
st.pyplot(fig)

# (5)
# Filttering the social apps
social_apps = ['Instagram', 'Facebook', 'X', 'WhatsApp', 'LinkedIn']
#Grouping and summing the usage minutes of each social app
social_apps_usage = df[df['App'].isin(social_apps)].groupby('App')['Usage_minutes'].sum()
# Total usage minutes for each social apps
total_social = social_apps_usage.sum()
# Total usage minutes for the gaming app.
total_game = df[df['App'] == '8 Ball Pool']['Usage_minutes'].sum()
# Key values
labels = ['Gaming App', 'Social Apps']
sizes = [total_game, total_social]
colors = ['red', 'blue']
st.markdown('#### 5. Distribution of Usage_minutes for gaming app (“8 Ball Pool”) vs. social apps')
#Plot a pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
st.pyplot(fig)

# (6)
# Resample the data to weekly frequency and caculate the total usage minutes
weekly_df = (df.groupby(['App', pd.Grouper(key='Date', freq='W')]).agg({'Usage_minutes': 'sum'}).reset_index())
st.markdown('#### 6. Total Screen Time for Netflix')
fig, ax = plt.subplots(figsize=(10, 6))
netflix_data = weekly_df[weekly_df['App'] == 'Netflix']
ax.plot(netflix_data['Date'], netflix_data['Usage_minutes'], label='Netflix')
ax.set_xlabel('Date', fontsize=15)
ax.set_ylabel('Usage_minutes', fontsize=15)
st.pyplot(fig)

##############################################################################################################################################################################################
# Insights and Reporting
st.subheader('Part 4: Summary')

st.markdown('#### Reporting')
st.write("""
- Analysis shows that the app usage that is most strongly influenced by notifications is Netflix.
- It is observed that Whatsapp has high notifications but low usage (ineffective notifications).
- From the result of the correlation between Times Opened and Usage_minutes for all apps (0.32), we can also say that there is a weak positive correlation between how often apps are opened and how long they are used. This means that users who open apps more frequently tend to spend slightly more time using them.
         """)

st.markdown('#### Insights')
st.markdown('##### Actionable insights users can adopt to encourage healthier digital habits')
st.write("In today's digital world, smartphones and apps have become deeply integrated into our daily routines. While technology offers convenience and connectivity, excessive screen time and constant app usage can negatively affect our mental well-being, productivity and sleep quality. To maintain a balanced and healthy relationship with technolog, it's important for users to be intentional about their digital habits. Below are some practical and effective steps you can take to develop healtheir app usage patterns and create more mindful screen time routines.")
st.write("""
        1.   Set daily screen time.
        2.   Turn off non-essential notifications.
        3.   Uninstall or mute high-usage and low-value apps.
        4.   Replace digital time with healthy alternatives such as taking a walk, reading a book or having offline social interactions.
         """)
############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
# Closing remark
closing_remark = st.button("Thank you for listening", on_click=st.balloons)
