import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Ini's Kitchen",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Ini's Kitchen App")
st.image(Image.open("Ini's Kitchen.jpg"))
st.header("Welcome to Ini's Kitchen")
st.write("We're thrilled to have you here! This is a place where every meal tells a delicious story from our Kitchen straight to your heart. If you are craving a hearty meal, we've got you covered. Explore our menu, place your order and let us take care of the rest.")

st.subheader("Features")

st.markdown("<p style='color:blue;'>1. Variety of Soup</p>", unsafe_allow_html=True)
st.write("What type of soup will you prefer?")
soups = ["Afang - N3,000","Ofe nsala - N8,000","Eforiro - N3,000","Banga/Atama - N3,000","Egusi - N3,000","Okro - N3,000","Fisherman - N8,000","Vegetable - 3,000","Stew - N2,500"]
selected_soup = st.multiselect("Please select one or more options?", soups)
if selected_soup:
     st.text_input(f"How many package do you need?")
else:
    st.markdown("<p style='color:red;'>You did not select any soup</p>", unsafe_allow_html=True)


st.markdown("<p style='color:blue;'>2. Variety of Rice</p>", unsafe_allow_html=True)
st.write("What type of rice will you prefer?")
rice = ["Fried - N3,000","Jollof - N3,000","White - N1,500","Coconut - N3,000","Native - N3,000","Masa - N2,000","Couscous - N2,000"]
selected_rice = st.multiselect("Please select one or more options?", rice)
if selected_rice:
    st.text_input(f"Number of packages?")
else:
    st.markdown("<p style='color:red;'>You did not select any rice</p>", unsafe_allow_html=True)


st.markdown("<p style='color:blue;'>3. Variety of Protein</p>", unsafe_allow_html=True)
st.write("What type of protein will you prefer?")
protein = ["Chicken - N3,000","Beef - N1,000","Goat - N2,500","Pork - N1,000","Snail - N2,500","Fish - N2,000","Egg(boiled or fried) - N1,000"]
selected_protein = st.multiselect("Please select one or more options?", protein)
if selected_protein:
    st.text_input(f"What quantity do you require?")
else:
    st.markdown("<p style='color:red;'>You did not select any protein</p>", unsafe_allow_html=True)


st.markdown("<p style='color:blue;'>4. Variety of Swallow</p>", unsafe_allow_html=True)
st.write("What type of swallow will you prefer?")
swallow = ["Pounded yam - N1,000","Semovita - N800","Eba - N500","Fufu - N500","Tuwon shinkafa - N800","Amala - N800","Starch - N600","Wheat - N800"]
selected_swallow = st.multiselect("Please select one or more options?", swallow)
if selected_swallow:
    st.text_input(f"How many wraps do you need?")
else:
    st.markdown("<p style='color:red;'>You did not select any swallow</p>", unsafe_allow_html=True)


selected_options = st.write("Note: You selected the following food", " - Soup", selected_soup, "Rice", selected_rice, "Protein", selected_protein, "Swallow", selected_swallow)

st.write("Thank you for your selection, please kindly provide your name and address in the space below")
st.text_input("Name, Address")
st.date_input('Select a Delivery Date')
st.time_input('What time will you like us to deliver your package?')


chkbx = st.checkbox("Do you have any dietary preferences or allergies we should note?")
if chkbx:
    st.text_area("Please put it down here")
else:
    st.write("")


order_conf = st.button("Would you like to proceed with the order?", on_click=st.balloons)
if order_conf:
    st.write("Thank you for choosing us!")
else:
    st.write("")


sidebar_title = st.sidebar.title("Ini's Kitchen Features")
service_rating = st.sidebar.select_slider("Can you rate our services?", options = list(range(1,11)))
food_category = st.sidebar.selectbox("Food Category", ["Soups","Rice","Protein","Swallow"])
promotion = st.sidebar.caption("There will be free deliveries for orders over N20,000 from May 27th to June 1st 2025 (only for those residing in Akwa Ibom State)")
special = st.sidebar.markdown("Special offers loading...")