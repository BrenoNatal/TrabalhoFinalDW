import pandas as pd


estacao_para_bairro = {
    'CA': 'Centro',
    'AV': 'Copacabana',
    'SC': 'São Cristóvão',
    'SP': 'Tijuca',
    'IR': 'Irajá',
    'BG': 'Bangu',
    'CG': 'Campo Grande',
    'PG': 'Pedra de Guaratiba'
}

estacao_para_zona = {
    'CA': 'Centro',
    'AV': 'Zona Sul',
    'SC': 'Centro',
    'SP': 'Zona Norte',
    'IR': 'Zona Norte',
    'BG': 'Zona Oeste',
    'CG': 'Zona Oeste',
    'PG': 'Zona Oeste'
}

estacao_para_ips = {
    'CA': 63.36,
    'AV': 82.35,
    'SC': 58.22,
    'SP': 79.48,
    'IR': 67.55,
    'BG': 58.59,
    'CG': 62.02,
    'PG': 49.02
}

estacao_para_ma = {
    'CA': 49.82,
    'AV': 40.20,
    'SC': 41.32,
    'SP': 51.28,
    'IR': 35.61,
    'BG': 33.99,
    'CG': 32.90,
    'PG': 35.64  
}


estacao_para_saude = {
    'CA': 70.46,
    'AV': 80.24,
    'SC': 59.86,
    'SP': 78.98,
    'IR': 69.17,
    'BG': 68.55,
    'CG': 70.48,
    'PG': 55.86
}


def categorizar(ur):
    if ur < 25:
        return 'Horrível'
    elif 25 <= ur < 50:
        return 'Ruim'
    elif 50 <= ur < 60:
        return 'Regular'
    elif 60 <= ur < 75:
        return 'Bom'
    elif 75 <= ur < 90:
        return 'Muito Bom'
    else:
        return 'Extremamente Bom'


def definir_local(estacao):
    return estacao_para_bairro.get(estacao, "Bairro não encontrada")

def definir_zona(estacao):
    return estacao_para_zona.get(estacao, "Zona não encontrada")

def definir_ips(estacao):
    return estacao_para_ips.get(estacao, "Zona não encontrada")

def definir_ma(estacao):
    return estacao_para_ma.get(estacao, "Zona não encontrada")

def definir_saude(estacao):
    return estacao_para_saude.get(estacao, "Zona não encontrada")


# Lê o arquivo CSV
df = pd.read_csv('C:\TrabalhoDW\qld_ar.csv')


DLocal = pd.DataFrame()

DLocal['estacao'] = df['estação']
DLocal['Bairro'] = df['estação'].apply(definir_local)
DLocal['Zona'] = df['estação'].apply(definir_zona)
DLocal['IPS'] = df['estação'].apply(definir_ips)
DLocal['qualidade_meio_ambiente'] = df['estação'].apply(definir_ma)
DLocal['saude_bem_estar'] = df['estação'].apply(definir_saude)



DLocal = DLocal.drop_duplicates()

# Aplica a categorização
DLocal['IPS'] = DLocal['IPS'].apply(categorizar) 
DLocal['qualidade_meio_ambiente'] = DLocal['qualidade_meio_ambiente'].apply(categorizar)
DLocal['saude_bem_estar'] = DLocal['saude_bem_estar'].apply(categorizar)

DLocal['pk_local'] = range(1, len(DLocal)+1)


DLocal.to_csv('DLocal.csv', index=False)









