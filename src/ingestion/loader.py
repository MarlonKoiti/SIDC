import pandas as pd
import re
from pathlib import Path


def padronizar_colunas(colunas):
    """
    Transforma nomes como 'NOME_MUNICIPIO_CIRCUNSCRICAO' ou 'COD IBGE'
    em 'nome_municipio_circunscricao' e 'cod_ibge'.
    """
    colunas_limpas = []
    for col in colunas:
        col = str(col).lower().strip()
        col = re.sub(r"[^a-z0-9]+", "_", col)
        colunas_limpas.append(col)
    return colunas_limpas


def iniciar_ingestao():
    bronze_path = Path("data/bronze/ocorrencias_brutas_jan.csv")
    silver_path = Path("data/silver/ocorrencias_padronizadas_janeiro.parquet")

    print(f"Iniciando leitura do arquivo Bronze: {bronze_path}")

    try:
        df = pd.read_csv(bronze_path, sep=";", encoding="iso-8859-1", low_memory=False)
    except FileNotFoundError:
        print(
            f"ERRO: Arquivo não encontrado no caminho {bronze_path}. Verifique o nome."
        )
        return
    except Exception:
        print("Falha ao ler com ponto e vírgula. Tentando com vírgula...")
        df = pd.read_csv(bronze_path, sep=",", encoding="iso-8859-1", low_memory=False)

    print(f"Sucesso! {len(df)} ocorrências carregadas na memória.")

    print("Padronizando nomenclaturas de colunas...")
    df.columns = padronizar_colunas(df.columns)

    print("Salvando na camada Silver em formato Parquet...")
    df.to_parquet(silver_path, index=False)

    print(f"Pipeline concluído. Dados limpos disponíveis em: {silver_path}")


if __name__ == "__main__":
    iniciar_ingestao()
