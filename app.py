import streamlit as st
import plotly.express as px

from utils import formata_valores

from dataset import receita, clientes, total_clientes, clientes_segmentacao, pedidos, ticket_m, porc_cancelamento, data, tipo_mais_fre
from graficos import grafico_top_mes,grafico_fre_compra,grafico_top_produtos,grafico_top_pais

##CONFIGURANDO TELA
st.set_page_config(layout='wide')

##MONTANDO PAG

st.title("Analise de Clientes")

##ABAS
aba1,aba2 = st.tabs(["Insigths","DataSet"])
with aba1:
    col1,col2,col3,col4,col5,col6, = st.columns(6)
    with col1:
        st.metric("Receita", formata_valores(receita),"R$")
    with col2:
        st.metric("Clientes", formata_valores(total_clientes))
    with col3:
        st.metric("Clientes", tipo_mais_fre)
    with col4:
        st.metric("Pedidos", formata_valores(pedidos))
    with col5:
        st.metric(label="Ticket Médio", value=f"R$ {ticket_m:,.2f}")
    with col6:
        st.metric("Taxa de Cancelamento", f"{porc_cancelamento:.1f}%")

    col7, col8 = st.columns(2)
    with col7:
        st.plotly_chart(grafico_fre_compra,width='content')
        st.plotly_chart(grafico_top_pais,width='content')

    with col8:
        st.plotly_chart(grafico_top_mes,width='content')
        st.plotly_chart(grafico_top_produtos,width='content')
    

#Aba2
with aba2:
    st.dataframe(data)