# Prompt de Relatório de Vendas (Empresa Meganium)

## Use Case

Você foi contatado para uma empresa chamada "Meganium Games" (fictícia) para Data Analyst (Analista de Dados) dentro dessa companhia. 

![alt text](image.png)

### Características 

- Ela é uma empresa que fabrica videogames, especificamente consoles portáteis
Os produtos são vendidos globalmente

![alt text](image-1.png)

- Tem quatro principais produtos com linhas diferentes de videogames

- A principal caracteristica dela é que foca especialmente na fabricação dos produtos, enquanto a distribuição e venda para terceiros (relação entre fabricante x e distribuitora y)

- Distribuidoras: AliExpress, Etsy e Shopee

### Problemas

1) Ela não tem a visão de controle de venda (por cada um dos terceiros seu próprio sistema de vendas), sendo o recomendado ter uma base histórica de vendas dos consoles em vários locais distintos

2) Como é uma empresa de fabricação somente, ela não consegue qual é o console mais popular (sem noção de saber a opinião pública para a questão da fabricação por oferta e demanda)


### Objetivos

1) Consolidar todas as bases de terceiros para realizar uma análise

2) Transformar dados de vendas e transformar em informações relevantes para a fabricante

3) Quais são os produtos mais populares em cada país
Como otimizar o processo de transporte e logística até o momento da venda

## Configuração dos diretórios

- [Data](./data/): diretório onde fica armazenado a base de dados das vendas das empresas distribuidoras
- [Prompts](./prompts/): Todos os prompts estão salvos aqui
- [Insights](./insights/): Tudo que for gerado a partir dos dados que foram trabalhados. É algo pode ir para o gerente, cliente final, coordenador, etc.
- [Scripts](./scripts/): Blocos de códigos feitos em Python para a análise dos dados brutos

