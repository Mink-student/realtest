import streamlit as st
import pickle
import numpy as np

st.title("ML Voorspellingsapp")

# Laad het model
@st.cache_resource
def laad_model():
    with open('model.pkl', 'rb') as f:
        return pickle.load(f)

model = laad_model()

# Inputvelden (pas aan op jouw data)
leeftijd = st.slider("Leeftijd", 18, 100, 30)
inkomen = st.number_input("Inkomen (€)", min_value=0.0, step=100.0)

if st.button("Voorspel"):
    input_data = np.array([[leeftijd, inkomen]])
    voorspelling = model.predict(input_data)
    st.success(f"Voorspelling: {voorspelling[0]}")
