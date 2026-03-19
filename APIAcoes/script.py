import os
import requests
import pandas as pd
from io import StringIO
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()
API_KEY = os.getenv('API_KEY')

def fetch_csv_from_api(url: str) -> pd.DataFrame:
    """Faz a requisição na API, trata possíveis erros e retorna um DataFrame."""
    try:
        response = requests.get(url + '&datatype=csv')
        response.raise_for_status() # Verifica se houve erro HTTP (ex: 404, 500)
        
        # Converte o texto CSV para DataFrame
        return pd.read_csv(StringIO(response.text))
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao conectar com a API: {e}")
        return pd.DataFrame() # Retorna um DataFrame vazio para não quebrar o código

def consultar_simbolo_empresa(empresa: str) -> str:
    """Busca o ticker (símbolo) da empresa na Alpha Vantage."""
    url = f'https://alphavantage.co/query?function=SYMBOL_SEARCH&keywords={empresa}&apikey={API_KEY}'
    df_search = fetch_csv_from_api(url)
    
    # Verifica se o DataFrame não está vazio e se a coluna existe
    if not df_search.empty and '1. symbol' in df_search.columns:
        return df_search['1. symbol'][0]
    return None

def consultar_dados_acao(symbol: str) -> pd.DataFrame:
    """Busca a cotação atual do símbolo informado."""
    url = f'https://alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}.SAO&apikey={API_KEY}'
    return fetch_csv_from_api(url)

def main():
    """Função principal que gerencia o estado do programa e a tabela."""
    # A tabela passa a ser uma variável local da execução principal (Morte ao "global"!)
    tabela_geral = pd.DataFrame()
    
    print("Bem-vindo ao Extrator de Dados da Alpha Vantage")
    
    while True:
        empresa = input("\nInsira a empresa que deseja consultar (ou 'sair' para encerrar): ").strip()
        
        if empresa.lower() == 'sair':
            print("Encerrando o programa...")
            break
            
        print(f"Buscando o ticker para '{empresa}'...")
        symbol = consultar_simbolo_empresa(empresa)
        
        if symbol:
            print(f"Ticker encontrado: {symbol}. Buscando cotação...")
            df_acao = consultar_dados_acao(symbol)
            
            if not df_acao.empty:
                # Concatena os novos dados à tabela principal
                tabela_geral = pd.concat([tabela_geral, df_acao], ignore_index=True)
                print("\nTabela Atualizada:")
                print(tabela_geral)
            else:
                print("Não foi possível obter a cotação neste momento.")
        else:
            print(f"Empresa '{empresa}' não encontrada ou limite da API atingido.")


if __name__ == "__main__":
    main()