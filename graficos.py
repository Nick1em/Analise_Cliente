import plotly.express as px


from dataset import data, vendas_por_data,periodo_compra,top_produto,top_pais



grafico_top_mes = px.bar(
    vendas_por_data,
    x = "mes",
    y = "total",
    text_auto=True,
    title="Meses que vais venderam",
)

grafico_fre_compra = px.line (
    periodo_compra,
    x = "Data",
    y = "total",
    title="Frequência: Periodo de Compras",
)

grafico_top_produtos = px.bar (
    top_produto,
    x = "Nome_curto",
    y = "Quantity",
    hover_data = {"Description": True},
    text_auto = True,
    title = "Produtos mais vendidos"
)

grafico_top_pais = px.bar (
    top_pais,
    x = "Country",
    y = "Receita",
    text_auto=True,
    title="Top por Receita"
)
