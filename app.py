import streamlit as st
import requests

st.set_page_config(page_title="Speech Summarizer",
                   initial_sidebar_state="expanded",
                   layout="wide")

url = "https://video-audio-summ-ext-abs-m67ja235na-ew.a.run.app/abs_ext_all_test"

'''
# Video Summarizer
'''

st.markdown(
'''Our application allows users to create a summary of a given speech on video or audio.
Simply use the features below and it will output an abstractive summary from your given media input.
    ''')

col1, col2 = st.columns(2)


with col1:

    form = col1.form(key="uploading")
    url_input = form.text_input("Video link", "http://")

    button = form.form_submit_button("Submit!")
    button

    params = {"url": url_input}

    if button:
        res = requests.get(url, params=params)
        text = res.json()
        #text["video_information"]["title"], text["video_information"]["duration"]
        text["abstractive_summary"]
        text["extractive_summary"]
        #summ = text['Summarized text']
        #col2.write(str(text))

with col2:
    """
    Here's your summaries
    """
