import requests
import streamlit as st
from datetime import datetime

date = datetime.today().strftime("%Y-%m-%d")
api_key = "h4pD8KlIHPk3cUDpCiUkcIk7qXD5Ph5R3feKoc6m"

# Form the API url using API key and current date
url=("https://api.nasa.gov/planetary/apod?"
     f"api_key={api_key}&"
     f"date={date}")

# Getting response from API
response = requests.get(url)
content = response.json()

# Getting title and explanation from JSON
title = content["title"]
explanation = content["explanation"]

# Using url from JSON get the image using API
image_url=content["url"]
response_image = requests.get(image_url)
image = response_image.content

# Write the image to file
with open("image.jpg", "wb") as file:
     file.write(image)

# Create the web page
st.header(title)
st.image("image.jpg")
st.write(explanation)