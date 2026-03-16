import pandas as pd
import win32com.client as win32

# importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar base de dados
pd.set_option('display.max_columns', None)

# faturamento por loja
tabela_faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

# quantidade de produtos vendidos por loja
tabela_produtos = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

# ticket médio por produto em cada loja
tabela_ticket_medio = (tabela_faturamento['Valor Final'] / tabela_produtos['Quantidade']).to_frame()
tabela_ticket_medio = tabela_ticket_medio.rename(columns={0:'Ticket Médio'})

# enviar um email (via outlook) com um relatório

outlook = win32.Dispatch('outlook.application')
mail - outlook.CreateItem(0)
mail.To = 'example@example.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>


<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{tabela_faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{tabela_produtos.to_html()}

<p>Ticket Médio dos Produtos:</p>
{tabela_ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>
<p>João Zanelato</p>
'''


mail.Send()