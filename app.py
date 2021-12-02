import streamlit as st
import requests


st.set_page_config(page_title="Speech Summarizer",
                   initial_sidebar_state="expanded")

url = "https://video-audio-summ-ext-abs-m67ja235na-ew.a.run.app/abs_ext_all_test"

'''
# Video Summarizer
'''

st.markdown(
'''Our application is an NLP-based application that allows users to generate a text summary based on a video.
Our model combines three pre-trained models: DeepSpeech, T5 and BERTSUM.
To try out our app, simply input a url here:
    ''')


form = st.form(key="uploading")
url_input = form.text_input("Video link", "http://")

button = form.form_submit_button("Submit!")
button

params = {"url": url_input}

st.markdown(
    """
    Our app will produce two different summaries:

    1) Extractive Summary

    2) Abstractive Summary
    """)

st.markdown(
''' ## Summaries:
    ''')
if button:
        #res = requests.get(url, params=params)
        #text = res.json()
        #text["video_information"]["title"], text["video_information"]["duration"]
        st.write("Abstractive Text: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, ")
        #st.write(text["abstractive_summary"])
        #text["extractive_summary"]
        st.write("Extractive Text: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, ")
        #st.write(text["abstractive_summary"])
        #summ = text['Summarized text']
        #st.write(str(text))


st.markdown(
''' ## Contact:
    ''')
st.markdown(
'''We are a group of Data Science students from Le Wagon Berlin. To learn more about our application, visit our Github Page: https://github.com/RafaKnabben/meeting_summarizer
    ''')
