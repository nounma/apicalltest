
import streamlit as st
import requests

'''
# Check on which plateform a movie is available?

'''
title= st.text_input("Title of the movie",value="batman")
country= st.text_input("Country",value="us")
if st.button('Search'):


    # enter here the address of your flask api
    url = "https://streaming-availability.p.rapidapi.com/v2/search/title"

    querystring = {"title":f"{title}",
                   "country":f"{country}",
                   "show_type":"movie",
                   "output_language":"en"}

    headers = {
        "X-RapidAPI-Key": "17e7083fbcmsh7bc96474b7bc9aep106984jsnb79c78943de8",
        "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    title_ok = response.json()["result"][0]["title"]
    overview = response.json()["result"][0]["overview"]
    cast = response.json()["result"][0]["cast"]
    trailer = response.json()["result"][0]["youtubeTrailerVideoLink"]
    streamingInfo = response.json()["result"][0].get(country, {}).get("streamingInfo")
    posterURLs = response.json()["result"][0]["posterURLs"]["154"]

    st.image(posterURLs,width = 154)
    st.write(title_ok)
    st.write(overview)
    st.write(cast)
    st.write(trailer)
    st.write(streamingInfo)


