import streamlit as st
from googletrans import Translator, constants

st.header('🔤 Translation App')

# Text input
st.subheader('Input')
text_input = st.text_area('Enter text to be translated ...')

# Language selection
languages_value = [i.capitalize() for i in constants.LANGUAGES.values()]
selected_language = st.selectbox('Translate to ...', languages_value)
selected_language_symbol = list(constants.LANGUAGES.keys())[list(constants.LANGUAGES.values()).index(selected_language.lower())]

# Initiate the Google API translator
translator = Translator()
translation = translator.translate(text_input, dest=selected_language_symbol)

st.header('Output')
st.info(translation.text)
