import streamlit as st
import plotly.express as px # graphing plotting library
from backend import get_data

# adit explains that when coding a program with a front end UI, the UI
# is usually coded first in a program like figma and then in streamlit
# and from there the backend is tied into the UI

# actual UI items
st.title("Weather Forecast for the next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
# above subheader incorporates data from the above variable such as place

# how to make a graph in streamlit, the 2 options are usually
# plotly and altair or bokeh are the main data visualization libraries
# in streamlit
try:
    if place:
    # getting temperature / sky data
        filtered_data = get_data(place, days)

        if option == "Temperature": #if statements will change what data
            # is being displayed in app based on the option selected
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            # above line gives a list of all 16 temperature values
            dates = [dict["dt_txt"] for dict in filtered_data]
            # above line gives a list of all 16 dates
        # create a temperature plot
            figure = px.line(x=dates, y=temperatures
                             , labels={"x": "Date", "y": "Temperature (C)"})
        # plotly line graph, dir(px) will show you all
        # possible plotly graphing options
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            # above is a dictionary relating a string to an image
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            # the above line will access the weather dict at [0], without [0]
            # you get Typeerror: slices not strings error
            image_paths = [images[nails]for nails in sky_conditions]
            # above line will create a list of the image paths that relate to
            # the sky_conditions key words of eg. sunny, rain, cloudy etc.
            # this is what is known as data translation
            print(sky_conditions)
            st.image(image_paths, width=80)
            # outputs weather images and where you can also change size
except KeyError:
    st.markdown("<h3 style='color: red;'>No City Found with that "
                "name Enter a valid City</h3>", unsafe_allow_html=True)
