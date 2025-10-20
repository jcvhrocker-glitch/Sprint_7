import streamlit as st
import pandas as pd
import plotly.graph_objects as go
car_data = pd.read_csv('vehicles_us.csv')
# crear botones para streamlit
hist_button = st.checkbox('Construir histograma')
scat_button_odo = st.checkbox('Construir scatter del odometro')
scat_button_model = st.checkbox('Construir scatter del precio')
# Crear un histograma utilizando plotly.graph_objects

# Se crea una figura vacía y luego se añade un rastro de histograma
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)
if scat_button_odo:
    st.write(
        'Creación de un scatter para el conjunto de datos de anuncios de venta de coches')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'],
                    y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly
    st.plotly_chart(fig, use_container_width=True)
if scat_button_model:
    st.write(
        'Creación de un scatter para el conjunto de datos de precio de venta de coches')
    fig = go.Figure(data=[go.Scatter(
        x=car_data['model_year'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre precio y año del coche')

    # Mostrar el gráfico Plotly
    st.plotly_chart(fig, use_container_width=True)
