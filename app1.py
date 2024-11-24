import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('C:/Users/ghora/OneDrive/Escritorio/my_project/my_first_repo/vehicles_us.csv')
st.header('Venta de Coches')
hist_button = st.checkbox('Construir Histograma')
hist_button1 = st.checkbox('Construir Gráfico de Dispersión')

if hist_button: 
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            fig = px.histogram(df, x="odometer")
        
            st.plotly_chart(fig, use_container_width=True)

elif hist_button1:
        st.write('Creación de un Gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
        fig = px.scatter(df, x="odometer", y="price")
        
        st.plotly_chart(fig, use_container_width=True)

else:
        st.write('Por favor, selecciona una opción para mostrar un gráfico')