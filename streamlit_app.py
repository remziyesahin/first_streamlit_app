import streamlit
import pandas


streamlit.title('My Parents New Healty Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list['Fruit']))
my_fruit_list = my_fruit_list.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)


#New section to display fruityvice api response
import requests
streamlit.header('Fruityvice Fruit Advice!')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

