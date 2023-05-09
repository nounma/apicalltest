
import streamlit as st

import datetime

import requests

'''
# TaxiFareModel front

This front queries the Le Wagon [taxi fare model API](https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2)
'''
prompt= st.text_input("Prompt",value="panda eating a banana")
negative_prompt= st.text_input("Negative Prompt",value="black and white image")
if st.button('Submit'):


    # enter here the address of your flask api
    url = "https://stablediffusionapi.com/api/v3/dreambooth"

    payload = {
     "key": "zNkopa4nVWcXhi1cbWyKygC8LuMqX9cvbX0qQRByQQhzLtRtXOU0WddKhr98",
     "model_id": "midjourney",
     "prompt": f"{prompt},DSLR photography, sharp focus,  Redshift, ((cinematic lighting)), f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, in-frame",
     "negative_prompt": f"{negative_prompt},painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",
     "width": "512",
     "height": "512",
     "samples": "1",
     "num_inference_steps": "30",
     "safety_checker": "no",
     "enhance_prompt": "yes",
     "seed": "null",
     "guidance_scale": 7.5,
     "webhook": "null",
     "track_id": "null"}
        
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", url, json=payload, headers=headers)
    image_link=response.json()['output'][0]
    st.image(image_link,width = 400)
