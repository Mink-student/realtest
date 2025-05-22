import streamlit as st
from pypmml import Model

# Titel
st.title("Machine Learning Voorspellingsapp")

# Laad het model (zorg dat model.pmml in dezelfde map zit)
@st.cache_resource
def laad_model():
    return Model.load('model.pmml')

model = laad_model()

# 🧾 Gebruikersinvoer (pas deze velden aan volgens jouw model)
leeftijd = st.slider("Leeftijd", min_value=18, max_value=100, value=30)
inkomen = st.number_input("Inkomen per maand (€)", min_value=0.0, step=100.0)

# Als er op de knop wordt geklikt:
if st.button("Voorspel"):
    input_data = {
        'leeftijd': leeftijd,
        'inkomen': inkomen
    }
    resultaat = model.predict(input_data)
    st.subheader("Voorspelling:")
    st.write(resultaat)
