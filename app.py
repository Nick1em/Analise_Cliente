import streamlit as st
import plotly.express as px

from dataset import receita, clientes, total_clientes, clientes_segmentacao, pedidos, ticket_m, porc_cancelamento, data, tipo_mais_fre


##CONFIGURANDO TELA
st.set_page_config(layout='wide')

##MONTANDO PAG

st.title("Analise de Clientes")

##ABAS
aba1,aba2 = st.tabs(["Insigths","DataSet"])
with aba1:
    col1,col2,col3,col4,col5,col6, = st.columns(6)
    with col1:
        st.metric("Receita", receita)
    with col2:
        st.metric("Clientes", total_clientes)
    with col3:
        st.metric("Clientes", tipo_mais_fre)
    with col4:
        st.metric("Pedidos", pedidos)
    with col5:
        st.metric("Ticket Médio", ticket_m)
    with col6:
        st.metric("Taxa de Cancelamento", porc_cancelamento)
    
#Aba2
with aba2:
    st.dataframe(data)