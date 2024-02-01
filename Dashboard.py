# bibliotecas -----------------------------
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from supabase import create_client

import os


# acessando o supabase -----------------------------
public_keys = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhlemdyaHRvcnNvYXlzcHduenNwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDUzNDM1NjIsImV4cCI6MjAyMDkxOTU2Mn0.ok_svjmVmQXpA1Eyp0oMsyMSehCbdC2g-ngWeaTg-6I'
url = 'https://xezgrhtorsoayspwnzsp.supabase.co'
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
    st.metric('Total Vendido no mês', formata_numero(10000, 'R$'))
with coluna2:

    st.metric('Comissão', formata_numero(10000*0.02, 'R$'))
with coluna3:
    
    st.metric('Quantidade de Vendas', formata_numero(2))

aba1, aba2 = st.tabs(['Mês Atual', "Planejamento"])

with aba1:
    st.title("Em Desenvolvimento")

with aba2:
    st.title("Em Desenvolvimento")