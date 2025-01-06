import os
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path
import pandera as pa
from sqlalchemy import create_engine

def load_settings():
    """Carrega as configurações a partir de variáveis de ambiente."""
    dotenv_path = Path.cwd() / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        "db_host": os.getenv("POSTGRES_HOST"),
        "db_user": os.getenv("POSTGRES_USER"),
        "db_pass": os.getenv("POSTGRES_PASSWORD"),
        "db_name": os.getenv("POSTGRES_DB"),
        "db_port": os.getenv("POSTGRES_PORT"),
    }

    # Converte db_port para inteiro, se não for None
    settings["db_port"] = int(settings["db_port"]) if settings["db_port"] else None
    
    return settings


def extrair_do_sql(query: str) -> pd.DataFrame:
    from app.schemas import ProdutoSchema  # Lazy import para evitar ciclo
    
    settings = load_settings()
    
    # Criar a string de conexão com base nas configurações
    connection_string = f"postgresql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"
    
    # Criar engine de conexão
    engine = create_engine(connection_string)
    
    with engine.connect() as conn, conn.begin():
        df = pd.read_sql(query, conn)
    
    # Validar o DataFrame com ProdutoSchema
    validated_df = ProdutoSchema.validate(df)
    return validated_df


if __name__ == "__main__":
    query = "SELECT * FROM bronze_produtos"
    df_crm = extrair_do_sql(query=query)
    print(df_crm)
