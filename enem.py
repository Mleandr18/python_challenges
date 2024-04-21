import pandas as pd

def dados_por_uf(path):
    """Carrega os dados do ENEM a partir de um arquivo CSV e salva separadamente por UF."""
    dados_enem = pd.read_csv(path) 
    ufs = dados_enem['SG_UF_ESC'].unique().tolist()
    for uf in ufs:
        dados_uf_filtrado = dados_enem[dados_enem['SG_UF_ESC'] == uf]
        df_uf = pd.DataFrame(dados_uf_filtrado)
        df_uf.to_csv(f'{uf}.csv', index=False)

caminho = 'enem2022.csv'
dados_por_uf(caminho)