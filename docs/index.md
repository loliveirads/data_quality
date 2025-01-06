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


## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
