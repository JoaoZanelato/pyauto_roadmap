import os
import shutil

#Lista o que está no diretório
arquivos = os.listdir()

#Caminho da pasta
#caminho = os.getcwd()

#print(caminho)
#print(arquivos)

#Renomear
#os.rename('Vendas - 1.xlsx', 'Vendas 1.xlsx')

#Mover
#os.rename('Vendas 1 - xlsx', 'Vendas\Vendas - 1.xlsx')

#Copiar
#shutil.copy2('Vendas 1 - xlsx', 'Vendas\Vendas - 1.xlsx')

for arquivo in arquivos:
    if 'xlsx' in arquivo:
        if "Compras" in arquivo:
            os.rename(arquivo, f'Compras\{arquivo}')
        elif "Vendas" in arquivo:
            os.rename(arquivo, f'Vendas\{arquivo}')
            