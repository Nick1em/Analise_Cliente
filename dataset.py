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
    bins=[0,2,9, float("inf")],
    labels=["Comum","Frequente",'VIP']
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

###KPI
receita = data['total'].sum()

ticket_m = receita / pedidos

