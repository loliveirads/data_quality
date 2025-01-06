# Documentação - Data Quality

```mermaid
graph TD;
A[Configura Variáveis] --> B[Ler o Banco SQL];
B -->|Sucesso| V[Validação do Schema de Entrada];
V -->|Falha| X[Alerta de Erro];
V -->|Sucesso| C[Transformar os KPIs];
C --> Y[Validação do Schema de Saída];
Y -->|Falha| Z[Alerta de Erro];
Y -->|Sucesso| D[Salvar no DuckDB];
```

## Contrato de dados

::: app.schemas.ProdutoSchema

## Ler o Banco

::: app.elt.extrair_do_sql

## Transformar os KPIs

::: app.etl.transformar

## Salvar no DuckDB

::: app.etl.load_to_duckdb
