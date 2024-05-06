import streamlit as st

st.title("Este es mi demo")
st.markdown("Esta es mi descripción")
#Crear barra deslizable
x = st.slider("Selecciona un valor ")

# Escribir
st.write(x, "el cuadrado es ", x*x)