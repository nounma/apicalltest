
import streamlit as st
import requests

'''
# Check on which plateform a movie is available!

'''
title= st.text_input("What is the movie title?",value="batman")
country= st.text_input("In which country to you want to watch?",value="us")
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
    for key, value in streamingInfo:
        stream_link = value[0]["link"]
        st.markdown("<a href='{}' target='_blank'><button>Click to watch the movie on "{}" </button></a>".format(stream_link, key), unsafe_allow_html=True)

    st.write(streamingInfo)
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
    cast_list = " ,".join([f" {actor}" for actor in cast])
    
    st.image(posterURLs,width = 400)
    st.write(title_ok," | ","Genre: ",genre," | ", runtime,"min")
    st.write("Director: ", director,"\n")
    st.write("Overview: ")
    st.markdown("<p style='font-weight:bold;'>{}</p>".format(tagline), unsafe_allow_html=True)
    st.write(overview)
    st.write("Actors: ",cast_list)
    st.markdown("<a href='{}' target='_blank'><button>Click to watch the trailer</button></a>".format(trailer), unsafe_allow_html=True)
    st.markdown("<a href='{}' target='_blank'><button style='background-color: red; color: white;'>Click to watch the movie</button></a>".format(streamingURL), unsafe_allow_html=True)



