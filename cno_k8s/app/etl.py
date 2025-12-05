import pandas as pd
import requests
from sqlalchemy import create_engine
import os

def extract_cno_data(url: str = "https://dados.gov.br/dataset/cno/resource/..."):  # Substitua pela URL real
    """Extrai dados CNO do portal."""
    df = pd.read_csv(url)
    df.to_csv('data/raw/cno_raw.csv', index=False)
    return df

def transform_data(df: pd.DataFrame):
    """Limpa e padroniza dados."""
    df['data_inicio'] = pd.to_datetime(df['data_inicio'], errors='coerce')
    df.dropna(subset=['id_obra'], inplace=True)
    return df

def load_data(df: pd.DataFrame, db_url: str = "sqlite:///cno.db"):
    """Carrega em SQLite."""
    engine = create_engine(db_url)
    df.to_sql('obras', engine, if_exists='replace', index=False)
