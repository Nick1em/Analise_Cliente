import pandas as pd


##CARREGANDO DADOS
data = pd.read_excel("data/online_retail_II.xlsx",engine='openpyxl')

##PADRONIZANDO DADOS
#Data
data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])
data = data.rename(columns={'InvoiceDate':'Data'})

sep_data = data.columns.drop("Data")

data[sep_data] = data[sep_data].astype(str)
##CONVERTENDO PARA NUMERICO
colunas = ['Invoice','Quantity','Price',]
data[colunas] = data[colunas].apply(pd.to_numeric, errors='coerce')

##Data para data
data["Data"] = pd.to_datetime(data["Data"])



#KPIs
total_clientes = data['Customer ID'].nunique()

clientes = (
    data
    .groupby("Customer ID")
    .size()
    .reset_index(name="Compras")
)
clientes["Categoria"] = pd.cut(
    clientes["Compras"],
    bins=[0,3,9, float("inf")],
    labels=["Comum","Frequente","VIP"]
)
clientes_segmentacao = (
    clientes["Categoria"]
    .value_counts()
    .reset_index()
)
pedidos = data['Invoice'].nunique()

tipo_mais_fre = clientes_segmentacao.iloc[0]["Categoria"]

cancelados = (data['Quantity'] <=0).sum()
total_pedidos = len(data)

porc_cancelamento = ( cancelados / total_pedidos) * 100

pedidos = data['Invoice'].nunique()
clientes_segmentacao.columns = ["Categoria", "Clientes"]

data = data [
    (data['Quantity'] > 0) &
    (data['Price'] > 0)
]
data["total"] = data['Quantity'] * data['Price']

##DataFrame para GF de linha 
periodo_compra =  ( 
    data.groupby("Data", as_index=False)["total"].sum()
)

##DataFrame para GF de barra mês q mais vendeu
data["mes"] = data["Data"].dt.to_period("M").astype(str)

vendas_por_data = (
    data.groupby("mes", as_index=False)['total']
    .sum()
    .head(5)
)

##Df para produtos mais vendidos
data["Nome_curto"] = data["Description"].apply(lambda x: x[:10] + '...' if len(x) > 10 else x)
top_produto = (
    data.groupby(["Nome_curto", "Description"], as_index=False)["Quantity"]
    .sum()
    .sort_values("Quantity", ascending=False)
    .head(6)
)

##DF para pais ue mais comprou
top_pais = (
    data.groupby("Country", as_index=False)["total"]
    .sum()
    .sort_values("total", ascending=False)
    .head(5)
    .rename(columns={"total":"Receita"})
)
###KPI
receita = data['total'].sum()

ticket_m = receita / pedidos


#print(top_pais)
