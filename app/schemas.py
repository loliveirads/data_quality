import pandera as pa
from pandera.typing import Series

class ProdutoSchema(pa.SchemaModel):
    id: Series[int] = pa.Field(ge=0, description="Identificador único do produto (não possui limite máximo).")
    titulo: Series[str] = pa.Field(nullable=False, description="Nome do produto.")
    descricao: Series[str] = pa.Field(nullable=True, description="Descrição do produto.")
    preco: Series[float] = pa.Field(ge=0.01, description="Preço do produto (deve ser maior que 0).")
    disponivel: Series[bool] = pa.Field(nullable=False, description="Disponibilidade do produto.")
    
    class Config:
        coerce = True



