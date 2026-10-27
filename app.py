# UI
import streamlit as st
from models import gemini_model

st.header('Gemini LLM')
st.subheader('Version - 3.8 Flash')

text = st.text_area('Enter prompt:',
             placeholder = 'Your prompt goes here...')
if st.button('Send✈️'):
    if text.strip()=='':
        st.warning('Please enter a valid prompt.')
    else:
        with st.spinner('Generating Content'):
            answer = gemini_model(text)
            st.toast('Content Generated.')
            st.write(answer)



