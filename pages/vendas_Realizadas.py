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

def compra_realizada(option = 'Adicionar'):
    if(option == 'Adicionar'):
        # Verifica se a combinação de subcategoria e categoria já existe
        
        condicoes_verificacao = (
    ('comprador', '==', comprador),
    ('nome_compra', '==', nome_compra),
    ('data_compra', '==', data_compra),
    ('valor_compra', '==',valor_compra),
    ('valor_compra','==',valor_compra),
    ('qtd_comprada','==',qtd_comprada)
        )

        # Criar uma instância de operação de seleção
        operacao_selecao = supabase.table('cadastro_vendas').select('*')

        # Adicionar condições de seleção
        for coluna, operador, valor in condicoes_verificacao:
            operacao_selecao = operacao_selecao.eq(coluna, valor)

        # Executar a seleção
        resultado_selecao = operacao_selecao.execute()

        # Verificar se existem registros que atendam às condições
        exists = len(resultado_selecao.data) > 0

        if not exists:  # Se não existir, adiciona
            data, count = supabase.table('cadastro_vendas').insert({
                "comprador": comprador,
                "nome_compra": nome_compra,
                'data_compra': data_compra.strftime("%d-%m-%Y"),
                "valor_compra": valor_compra,
                "qtd_comprada": qtd_comprada,
                "obs": obs,
                "apelido_pf": apelido_pf
            }).execute()
            sucesso = st.success('Venda cadastrada com sucesso!', icon="✅")
            time.sleep(5)
        else:
            sucesso = st.warning('Esta venda já existe.')
            time.sleep(5)
    else:
        condicoes_exclusao = (
            ('comprador', '==', comprador),
            ('nome_compra', '==', nome_compra),
            ('data_compra', '==', data_compra)
            )
        operacao_exclusao = supabase.table('cadastro_vendas').delete()
        for coluna, operador, valor in condicoes_exclusao:
            operacao_exclusao = operacao_exclusao.eq(coluna, valor)

            # Executar a exclusão
            data, count = operacao_exclusao.execute()
        sucesso = st.success('Venda removida com sucesso!', icon="❌")
        time.sleep(5)

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
st.markdown("#### Controle de Vendas:")

aba1, aba2 = st.tabs(['Cadastro de Vendas','Visualização das Vendas'])
with aba1:
    coluna1, coluna2, coluna3 = st.columns(3)
    with coluna1:
        select_comprador_pj = pd.DataFrame.from_dict(supabase.table('cadastro_pj').select('razao_social').execute().data)
        select_comprador_pf = pd.DataFrame.from_dict(supabase.table('cadastro_pf').select('nome_pf').execute().data)
        comprador_nomes = tuple(select_comprador_pj['razao_social'].unique().tolist() + select_comprador_pf['nome_pf'].unique().tolist())
        comprador = st.selectbox("Nome/Razão Social:*",comprador_nomes, help="A razão Social ou Nome Pessoa Física precisa estar cadastrado na sua base de dados")                
    with coluna2:
        nome_compra = st.text_input("Nome da Pessoa física que realizou a compra:*", 'Nome Completo', key='nome_pf_compra')
    with coluna3:
        apelido_pf = st.text_input("Apelido:", '', key='apelido_pf' )
    coluna1, coluna2, coluna3 = st.columns(3)
    with coluna1:
        default_date = datetime.now()
        data_compra = st.date_input("Data em que a compra foi realizada:", key="date_compra_input", value=default_date)
    with coluna2:
        valor_compra = st.number_input("Valor da compra:*", key= 'valor_compra')
    with coluna3:
        qtd_comprada = st.number_input("Quantidade de produtos comprados:*", value=1, step=1, key='qtd_produtos')
    obs = st.text_input("Alguma informação adicional:")

    st.markdown("___")
    coluna3, coluna1, coluna2, coluna4 = st.columns(4)
    with coluna1:
        # Adicionando o botão sem usar on_click
        if st.button('✔️ Cadastrar uma nova Venda.'):
            if(nome_compra == "Nome Completo"):
                st.warning("❗ Cadastre uma venda realizada")
            else:
                compra_realizada(option = 'Adicionar')
        
        
    with coluna2:
        # Adicionando o botão sem usar on_click
        if st.button('❌ Excluir uma Venda.'):        
            if(nome_compra == "Nome Completo"):
                st.warning("❗ Cadastre uma venda realizada")
            else:
                compra_realizada(option = 'Excluir')

with aba2:
    df_venda = pd.DataFrame.from_dict(supabase.table('cadastro_vendas').select('*').execute().data)
    nome_colunas = {
        "comprador": 'Empresa',
        "nome_compra": 'Nome do Cliente',
        'data_compra': 'Data da Compra',
        "valor_compra": 'Valor Vendido',
        "qtd_comprada": 'Quantidade de Produtos',
        "obs": 'Informações',
        "apelido_pf": 'Apelido'
    }
    df_venda = df_venda.rename(columns=nome_colunas)

    # Exibindo o DataFrame usando o método st.table()
    width = 800
    if (df_venda.shape[1] >=1):
        st.markdown(
            f'<div style="margin:auto; width:{width}px; ">'
            f'{df_venda.to_html(classes="dataframe")}'
            '</div>',
            unsafe_allow_html=True
        )


