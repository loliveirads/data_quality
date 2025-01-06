import pandera as pa
from pandera.typing import Series

class ProdutoSchema(pa.SchemaModel):
    """
    Esquema de validação para um DataFrame de produtos.

    Attributes:
        id_produto (int): Identificador único do produto.
        nome (str): Nome do produto.
        quantidade (int): Quantidade em estoque do produto. Deve ser no mínimo 20 e no máximo 200.
        preco (float): Preço do produto. Deve ser maior que 0, sem limite máximo.
        categoria (str): Categoria à qual o produto pertence.
    """
    
    id_produto: Series[int] = pa.Field(ge=0, description="Identificador único do produto (sem limite máximo).")
    nome: Series[str] = pa.Field(nullable=False, description="Nome do produto.")
    quantidade: Series[int] = pa.Field(ge=20, le=200, description="Quantidade em estoque (20 a 200).")
    preco: Series[float] = pa.Field(ge=0.01, description="Preço do produto (deve ser maior que 0).")
    categoria: Series[str] = pa.Field(nullable=False, description="Categoria do produto.")
    
    class Config:
        coerce = True  # Força a conversão dos tipos
        strict = True  # Garante que apenas colunas definidas no schema sejam aceitas
