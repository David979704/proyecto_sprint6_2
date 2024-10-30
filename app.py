import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos con la ruta correcta
car_data = pd.read_csv('vehicles_us.csv')

# Crear el primer botón para construir el histograma
hist_button = st.button('Construir histograma')

# Crear el segundo botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

# Al hacer clic en el botón del histograma
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Al hacer clic en el botón del gráfico de dispersión
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price", title="Gráfico de dispersión de kilometraje vs precio")
    st.plotly_chart(fig, use_container_width=True)
