import streamlit as st
from pydub import AudioSegment
import requests

st.markdown('''## Video Audio Summarizer
''')

url = "https://test--2511-m67ja235na-ew.a.run.app/all_steps_test"

form = st.form(key="uploading")
url_input = form.text_input("Video link", "http://")

button = form.form_submit_button("Submit!")
button

params = {"url": url_input}

CSS_summary = """
    p {
        background-color: 'red'
    }
"""

def capital_letters(text):
    capitalized = ""
    if text[0] != text[0].capitalize():
        capitalized = capitalized + text[0].capitalize()
        text = text[1:]

    for num in range(len(text)):
        if text[num - 2] + text[num - 1] != ". ":
            capitalized = capitalized + text[num]
        if text[num - 2] + text[num - 1] == ". ":
            capitalized = capitalized + text[num].capitalize()

    return capitalized

if button:
    res = requests.get(url, params=params)
    text = res.json()
    summ = text['Summarized text']
    summ = capital_letters(summ)
    st.write(str(summ), f'<style>{CSS_summary}</style>', unsafe_allow_html=True)
