import pandas as pd

# Leitura de arquivos

# Caminhos dos arquivos
files = {
    "AliExpress": "/mnt/data/Meganium_Sales_Data_-_AliExpress.csv",
    "Etsy": "/mnt/data/Meganium_Sales_Data_-_Etsy.csv",
    "Shopee": "/mnt/data/Meganium_Sales_Data_-_Shopee.csv",
}

# Carregar os arquivos
dataframes = {platform: pd.read_csv(path) for platform, path in files.items()}

# Verificar as primeiras linhas de cada dataframe
data_overview = {platform: df.head() for platform, df in dataframes.items()}
data_overview

# Prompt 1

# Concatenar todos os dados em um único dataframe
combined_df = pd.concat(dataframes.values())

# Agrupar por produto e país, somando as quantidades vendidas
summary = combined_df.groupby(["product_sold", "delivery_country"])["quantity"].sum().reset_index()

# Renomear colunas para melhor compreensão
summary.columns = ["Produto", "País", "Quantidade Vendida"]

# Ordenar os dados para melhor visualização
summary = summary.sort_values(by=["Produto", "Quantidade Vendida"], ascending=[True, False])

summary


# Prompt 2

# Selecionar o produto com maior quantidade de venda para cada país
top_products_per_country = summary.loc[summary.groupby("País")["Quantidade Vendida"].idxmax()]

# Ordenar por país para melhor visualização
top_products_per_country = top_products_per_country.sort_values(by="País")

top_products_per_country

# Prompt 3

from datetime import datetime

# Adicionar coluna de idade aos dataframes originais
current_year = datetime.now().year

for platform, df in dataframes.items():
    df["buyer_birth_date"] = pd.to_datetime(df["buyer_birth_date"], errors="coerce")
    df["buyer_age"] = current_year - df["buyer_birth_date"].dt.year

# Concatenar novamente os dados com a nova coluna de idade
combined_df = pd.concat(dataframes.values())

# Filtrar apenas os produtos mais vendidos por país
top_products = top_products_per_country["Produto"].unique()
filtered_df = combined_df[combined_df["product_sold"].isin(top_products)]

# Criar faixas de idade de 5 em 5 anos
filtered_df["age_group"] = (filtered_df["buyer_age"] // 5) * 5

# Calcular a média de idade por produto e faixa etária
avg_age_per_product = (
    filtered_df.groupby(["product_sold", "age_group"])["buyer_age"]
    .mean()
    .reset_index()
    .sort_values(by=["product_sold", "age_group"])
)

avg_age_per_product

# Prompt 4.1

from datetime import datetime

# Adicionar coluna de idade aos dataframes originais
current_year = datetime.now().year

for platform, df in dataframes.items():
    df["buyer_birth_date"] = pd.to_datetime(df["buyer_birth_date"], errors="coerce")
    df["buyer_age"] = current_year - df["buyer_birth_date"].dt.year

# Concatenar novamente os dados com a nova coluna de idade
combined_df = pd.concat(dataframes.values())

# Filtrar apenas os produtos mais vendidos por país
top_products = top_products_per_country["Produto"].unique()
filtered_df = combined_df[combined_df["product_sold"].isin(top_products)]

# Criar faixas de idade de 5 em 5 anos
filtered_df["age_group"] = (filtered_df["buyer_age"] // 5) * 5

# Calcular a média de idade por produto e faixa etária
avg_age_per_product = (
    filtered_df.groupby(["product_sold", "age_group"])["buyer_age"]
    .mean()
    .reset_index()
    .sort_values(by=["product_sold", "age_group"])
)

avg_age_per_product

# Prompt 4.2

# Agrupar por plataforma (vendedora) e somar todas as vendas
total_sales_per_platform = combined_df.groupby("site")["quantity"].sum().reset_index()
total_sales_per_platform.columns = ["Plataforma", "Total de Consoles Vendidos"]

# Agrupar por plataforma e produto, somando as vendas individuais de cada console
sales_per_platform_product = combined_df.groupby(["site", "product_sold"])["quantity"].sum().reset_index()
sales_per_platform_product.columns = ["Plataforma", "Produto", "Quantidade Vendida"]

total_sales_per_platform, sales_per_platform_product


# Prompt 5.1

# Converter datas para DateTime
combined_df["date"] = pd.to_datetime(combined_df["date"], errors="coerce")

# Criar colunas de Ano e Semestre
combined_df["Year"] = combined_df["date"].dt.year
combined_df["Semester"] = combined_df["date"].dt.month.apply(lambda x: 1 if x <= 6 else 2)

# Calcular o lucro líquido total por console
total_profit_per_console = (
    combined_df.groupby("product_sold")[["total_price", "discount_applied"]]
    .sum()
    .reset_index()
)
total_profit_per_console["Lucro Líquido (USD)"] = (
    total_profit_per_console["total_price"] - total_profit_per_console["discount_applied"]
)
total_profit_per_console = total_profit_per_console[["product_sold", "Lucro Líquido (USD)"]]

# Calcular o lucro líquido por console, ano e semestre
profit_per_console_semester = (
    combined_df.groupby(["product_sold", "Year", "Semester"])[["total_price", "discount_applied"]]
    .sum()
    .reset_index()
)
profit_per_console_semester["Lucro Líquido (USD)"] = (
    profit_per_console_semester["total_price"] - profit_per_console_semester["discount_applied"]
)
profit_per_console_semester = profit_per_console_semester[["product_sold", "Year", "Semester", "Lucro Líquido (USD)"]]

total_profit_per_console, profit_per_console_semester

# Verificar as colunas disponíveis no dataset
combined_df.columns


# Prompt 5.2

# Calcular o lucro líquido total por console usando "discount_value"
total_profit_per_console = (
    combined_df.groupby("product_sold")[["total_price", "discount_value"]]
    .sum()
    .reset_index()
)
total_profit_per_console["Lucro Líquido (USD)"] = (
    total_profit_per_console["total_price"] - total_profit_per_console["discount_value"]
)
total_profit_per_console = total_profit_per_console[["product_sold", "Lucro Líquido (USD)"]]

# Calcular o lucro líquido por console, ano e semestre
profit_per_console_semester = (
    combined_df.groupby(["product_sold", "Year", "Semester"])[["total_price", "discount_value"]]
    .sum()
    .reset_index()
)
profit_per_console_semester["Lucro Líquido (USD)"] = (
    profit_per_console_semester["total_price"] - profit_per_console_semester["discount_value"]
)
profit_per_console_semester = profit_per_console_semester[["product_sold", "Year", "Semester", "Lucro Líquido (USD)"]]

total_profit_per_console, profit_per_console_semester
