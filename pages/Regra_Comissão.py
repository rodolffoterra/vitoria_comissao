# bibliotecas -----------------------------
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from supabase import create_client
from datetime import datetime
import time
import os


# acessando o supabase -----------------------------
public_keys = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJkY2xpaHFob3l2Z3B1dGV6dGhtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDY3ODg0MTMsImV4cCI6MjAyMjM2NDQxM30.mVwtKVYyyDmaKqaf-tyzmHF1u8IxuVIUE1Il2YNGSE4'
url = 'https://bdclihqhoyvgputezthm.supabase.co'
url = os.environ.get('SUPABASE_URL', url)  # Use 'SUPABASE_URL' as the environment variable name
key = os.environ.get('SUPABASE_KEY', public_keys)  # Use 'SUPABASE_KEY' as the environment variable name
supabase = create_client(url, key)

# dicionário de meses

mes = {
    'Janeiro':'01',
     'Fevereiro':'02',
     'Março':'03',
     'Abril':'04',
     'Maio':'05',
     'Junho':'06',
     'Julho':'07',
     'Agosto':'08',
     'Setembro':'09',
     'Outubro':'10',
     'Novembro':'11',
     'Dezembro':'12'
     }

#Função -----------------------------
def formata_numero(valor, prefixo = ''):
    for unidade in ['','mil']:
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /=1000
    return f'{prefixo} {valor:.2f} milhões'

#configuração -----------------------------
st.set_page_config(layout= 'wide')

#Sidebar -----------------------------

st.sidebar.markdown("<h1 style='text-align: center;'>Vendedora</h1>", unsafe_allow_html=True)
st.sidebar.image('img/vitoria.png', width=30, caption="Vitória", use_column_width=True)
st.sidebar.markdown("___")

st.sidebar.markdown("<div style='text-align: center;'><a href='https://www.a2ttechnology.com.br/' class='button'>A2T Technology</a></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='text-align: center;'><img src='https://static.wixstatic.com/media/cc8e7f_9a50acb7aee44699a2d15f74292c5c39~mv2.png/v1/fill/w_327,h_236,al_c,q_85,enc_auto/cc8e7f_9a50acb7aee44699a2d15f74292c5c39~mv2.png' alt='logo' width='150' height='98'></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='text-align: center;'><a href='https://api.whatsapp.com/send?phone=5515992630395' class='button'><i class='fab fa-whatsapp'></i> Whatsapp</a></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='text-align: center;'><br></br></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='text-align: center;'><p>©2024 Todos os direito reservados.</p></div>", unsafe_allow_html=True)

# tabelas

#Body -----------------------------

coluna1, coluna2, coluna3 = st.columns(3)
with coluna1:
    st.metric('Total Vendido no mês:', formata_numero(10000, 'R$'))
with coluna2:

    st.metric('Comissão:', formata_numero(10000*0.02, 'R$'))
with coluna3:
    
    st.metric('Quantidade de Vendas:', 2)

st.markdown("___")
st.markdown("#### Cadastro de meta para comissão:")


mes_traducao = {
    'January': 'Janeiro',
    'February': 'Fevereiro',
    'March': 'Março',
    'April': 'Abril',
    'May': 'Maio',
    'June': 'Junho',
    'July': 'Julho',
    'August': 'Agosto',
    'September': 'Setembro',
    'October': 'Outubro',
    'November': 'Novembro',
    'December': 'Dezembro'
}

# Exemplo de uso:
mes_atual_ingles = datetime.now().strftime('%B')
mes_atual_portugues = mes_traducao.get(mes_atual_ingles, mes_atual_ingles)
percentual = ['1%','2%','3%','4%','5%','6%','7%','8%','9%','10%','11%','12%','13%','14%','15%']
meta_percentual = ['10%','15%','20%','25%','30%','35%','40%','45%','50%','55%','60%','65%','70%','75%','80%', '85%','90%','95%','100%','Acima de 100%']


coluna1, coluna2, coluna3, coluna4 = st.columns(4) 
with coluna1:
    mes_comissao = st.selectbox("Mês que será virgente Comissão:", mes.keys(), index =list(mes.keys()).index(mes_atual_portugues), key = "faixa_01_01")    
with coluna2:
    valor_meta = st.number_input(f"Mês de comissão para o mês de {mes_comissao}:",value = 10000.00, key = 'faixa_01_02')     
with coluna3:
    percentual_comissao_01 = st.selectbox("1ª) Percentual:", percentual, index = percentual.index('2%'), key = 'faixa_01_03')    
with coluna4:
    percentual_meta_01 = st.selectbox("1ª) Faixa da Meta:", meta_percentual, index = meta_percentual.index('30%'), key = 'faixa_01_04')

coluna1, coluna2, coluna3, coluna4, coluna5, coluna6, coluna7, coluna8 = st.columns(8) 
with coluna1:
    percentual_comissao_02 = st.selectbox("2ª) Percentual:", percentual, index = percentual.index('3%'), key = 'faixa_02_01')         

with coluna2:
    percentual_meta_02 = st.selectbox("2ª) Faixa da Meta:", meta_percentual, index = meta_percentual.index('50%'), key = 'faixa_02_02')
    
with coluna3:
    percentual_comissao_03 = st.selectbox("3ª) Percentual:", percentual, index = percentual.index('4%'), key = 'faixa_03_01')   
with coluna4:
    percentual_meta_03 = st.selectbox("3ª) Faixa da Meta:", meta_percentual, index = meta_percentual.index('70%'), key = 'faixa_04_04')  

with coluna5:
    percentual_comissao_04 = st.selectbox("4ª) Percentual:", percentual, index = percentual.index('5%'), key = 'faixa_04_01')   

with coluna6:
    percentual_meta_04 = st.selectbox("4ª) Faixa da Meta:", meta_percentual, index = meta_percentual.index('100%'), key = 'faixa_04_02')
    
with coluna7:
    percentual_comissao_05 = st.selectbox("5ª) Percentual:", percentual, index = percentual.index('7%'), key = 'faixa_03_041111')   
with coluna8:
    percentual_meta_05 = st.selectbox("5ª) Faixa da Meta:", meta_percentual, index = meta_percentual.index('Acima de 100%'), key = 'faixa_4_04444')  
st.markdown("___")

data = {'Informação': [f'Meta para {mes_comissao} / {datetime.now().year}',f'Total meta: R$ {valor_meta}', 'Comissão'],
        percentual_comissao_01:[ percentual_meta_01, valor_meta*float(str(percentual_meta_01).replace("%",''))/100, (valor_meta*float(str(percentual_meta_01).replace("%",''))/100)*(float(str(percentual_comissao_01).replace("%",''))/100)],
        percentual_comissao_02:[ percentual_meta_02 , valor_meta*float(str(percentual_meta_02).replace("%",''))/100, (valor_meta*float(str(percentual_meta_02).replace("%",''))/100)*(float(str(percentual_comissao_02).replace("%",''))/100)],
        percentual_comissao_03:[ percentual_meta_03 , valor_meta*float(str(percentual_meta_03).replace("%",''))/100, (valor_meta*float(str(percentual_meta_03).replace("%",''))/100)*(float(str(percentual_comissao_03).replace("%",''))/100)],
        percentual_comissao_04:[ percentual_meta_04 , valor_meta*float(str(percentual_meta_04).replace("%",''))/100, (valor_meta*float(str(percentual_meta_04).replace("%",''))/100)*(float(str(percentual_comissao_04).replace("%",''))/100)],
        percentual_comissao_05:[ percentual_meta_05 , f'Acima de R$ {valor_meta}', 'R$ -']}
df = pd.DataFrame(data)
width = 800
st.markdown(
        f'<div style="margin:auto; width:{width}px; ">'
        f'{df.to_html(classes="dataframe")}'
        '</div>',
        unsafe_allow_html=True
    )


