
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
    streamingInfo = response.json()["result"][0]["streamingInfo"][f"{country}"]
    streamingInfo_first_value = list(streamingInfo.values())[0]
    streamingURL = streamingInfo_first_value[0]["link"]
    title_ok = response.json()["result"][0]["title"]
    overview = response.json()["result"][0]["overview"]
    cast = response.json()["result"][0]["cast"]
    tagline = response.json()["result"][0]["tagline"]
    trailer = response.json()["result"][0]["youtubeTrailerVideoLink"]
    posterURLs = response.json()["result"][0]["posterURLs"]["500"]
    genre = response.json()["result"][0]["genres"][0]["name"]
    director = response.json()["result"][0]["directors"][0]
    runtime = response.json()["result"][0]["runtime"]
    cast_list = "\n".join([f"{actor}" for actor in cast])
    
    st.image(posterURLs,width = 400)
    st.write(title_ok,genre, runtime, sep=" | ")
    st.write(director)
    st.write(tagline)
    st.write(overview)
    st.write(cast_list)
    st.write(trailer)
    st.write(streamingURL)


