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

def mensagem_sucesso(name_tb, option = 'Adicionar'):
    if (name_tb == "cadastro_pj"):
        if(option == 'Adicionar'):
            # Verifica se a combinação de subcategoria e categoria já existe
            exists =  supabase.table('cadastro_pj').select('razao_social').eq('razao_social', razao_social).execute()
            if not exists.data:  # Se não existir, adiciona
                data, count = supabase.table('cadastro_pj').insert({"razao_social": razao_social,
                                                                     "cnpj":cnpj,
                                                                     "insc_estadual":insc_estadual_pj,
                                                                     "fundado": data_fundacao.strftime("%Y-%m-%d"),
                                                                     "tel_01_pj":tel_01_pj,
                                                                     "cel_02_pj":cel_02_pj,
                                                                     "zap": zap_pj,
                                                                     "email": email_pj,
                                                                     "cep_pj":cep_pj,
                                                                     "end_pj":end_pj,
                                                                     "compl_pj":compl_pj,
                                                                     "cidade_pj":cidade_pj,
                                                                     "uf_pj": uf_pj,
                                                                     "especialidade": especialidade
                                                                     }).execute()
                sucesso = st.success('Razão Social cadastrada com sucesso!', icon="✅")
                time.sleep(5)
            else:
                sucesso = st.warning('Este Razão Social já existe.')
            time.sleep(5)
        else:
            data, count = supabase.table('cadastro_pj').delete().eq('razao_social', razao_social).execute()
            sucesso = st.success('Razão Social removida com sucesso!', icon="❌")
            time.sleep(5)
    else:
        if(option == 'Adicionar'):
            # Verifica se a combinação de subcategoria e categoria já existe
            exists =  supabase.table('cadastro_pf').select('nome_pf').eq('nome_pf', nome_pf).execute()
            if not exists.data:  # Se não existir, adiciona
                data, count = supabase.table('cadastro_pf').insert({"razao_social":razao_social_pf,
                                                                    "nome_pf": nome_pf,
                                                                     "apelido_pf":apelido_pf,
                                                                     "sexo": sexo,
                                                                     "cpf_pf": cpf_pf,
                                                                     'rg_pf': rg_pf,
                                                                     'data_nasc_pf': data_nasc_pf.strftime("%Y-%m-%d"),
                                                                     "tel_01_pf":tel_01_pf,
                                                                     "tel_02_pf":tel_02_pf,
                                                                     "email_pf": email_pf,
                                                                     "cep_pf":cep_pf,
                                                                     "end_pf":end_pf,
                                                                     "compl_pf":compl_pf,
                                                                     "cidade_pf":cidade_pf,
                                                                     "uf_pf": uf_pf
                                                                     }).execute()
                sucesso = st.success('Pessoa Física cadastrada com sucesso!', icon="✅")
                time.sleep(5)
            else:
                sucesso = st.warning('Este nome já existe.')
            time.sleep(5)
        else:
            data, count = supabase.table('cadastro_pf').delete().eq('nome_pf', nome_pf).execute()
            sucesso = st.success('Pessoa Física removida com sucesso!', icon="❌")
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

aba1, aba2, aba3 = st.tabs(['Cadastro de Cliente', "Pessoa Jurídica", "Pessoa Física"])

with aba1:
    st.markdown("#### Cadastro de Clientes:")

    st.markdown("##### Pessoa Jurídica:")
    with st.expander("Informações Cadastrais"):

        coluna1, coluna2, coluna3 = st.columns([3,2,1])
        with coluna1:
            razao_social = st.text_input("Razão Social:*", 'Razão Social ou Nome Fantasia')
        with coluna2:
            cnpj = st.text_input("CNPJ:*", key="cnpj_input", help="00.000.000/0001-00")
        with coluna3:
            insc_estadual_pj = st.text_input("INSC. Estadual:*", '')

        coluna1, coluna2, coluna3 = st.columns([1,2,2])
        with coluna1:
            default_date = datetime.now()
            data_fundacao = st.date_input("Fundado em:", key="date_input", value=default_date)
        with coluna2:
            coluna2_01, coluna2_02 = st.columns(2)
            with coluna2_01:
                tel_01_pj = st.text_input("Telefone Comercial:", '', key = 'tel_01_pj', help="Ex.: (61) 3303-4671")
            with coluna2_02:
                cel_02_pj = st.text_input("Celular:", '', key = 'tel_02_pj', help="Ex.: (61) 9.3303-4671")
        with coluna3:
            coluna2_01, coluna2_02 = st.columns([1,4])
            with coluna2_01:
                zap_pj = uf = st.selectbox("Whatsapp:*", ['Sim','Não'], index=0)
            with coluna2_02:
                email_pj = st.text_input("E-mail:*", '', help="rodolfoterratechnology@gmail.com")

        coluna1, coluna2, coluna3, coluna4, coluna5 = st.columns([1,4,1,3,1])
        with coluna1:
            cep_pj = st.text_input("CEP:*", '',help="Ex.: 09721-230")
        with coluna2:
            end_pj = st.text_input("Endereço:*", '')
        with coluna3:
            compl_pj = st.text_input("Complemento:", '')
        with coluna4:
            cidade_pj = st.text_input("Cidade:*", '')
        with coluna5:
            ufs = ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO')
            uf_pj = st.selectbox("UF:*", ufs, index=ufs.index('SP'))
        especialidade = st.radio("Especialidade:*",
            ["Médico",'Dentista','Farmacéutico','Biomédico','Esteticista','Enfermeiro ','Fisioterapeuta','Outros'], horizontal=True)
        st.markdown("<div style='text-align: center;'><br></br></div>", unsafe_allow_html=True)
        coluna3, coluna1, coluna2, coluna4 = st.columns(4)
        with coluna1:
            # Adicionando o botão sem usar on_click
            if st.button('✔️ Cadastrar uma nova Razão Social.'):
                if(razao_social == "Razão Social ou Nome Fantasia"):
                    st.warning("❗ Escreva o nome da razão social")
                else:
                    mensagem_sucesso('cadastro_pj', option = 'Adicionar')
            
            
        with coluna2:
            # Adicionando o botão sem usar on_click
            if st.button('❌ Excluir uma Razão Social existente.'):        
                if(razao_social == "Razão Social ou Nome Fantasia"):
                    st.warning("❗ Escreva o nome da razão social")
                else:
                    mensagem_sucesso('cadastro_pj', option = 'Excluir')

    st.markdown("___")
    st.markdown("##### Pessoa Física:")
    with st.expander("Informações Cadastrais"):

        coluna1, coluna2, coluna3, coluna4, coluna5 = st.columns([5,2,2,1,1])
        with coluna1:
            coluna1_01, coluna1_02 = st.columns([2,3])
            with coluna1_01:
                select_razao_social = pd.DataFrame.from_dict(supabase.table('cadastro_pj').select('razao_social').execute().data)
                select_razao_social = tuple([''] + select_razao_social['razao_social'].unique().tolist())
                razao_social_pf = st.selectbox("Razão Social:*",select_razao_social, help="Caso queira cadastrar uma pessoa Física que esteja associada a um CNPJ já cadastrado ")
            with coluna1_02:
                nome_pf = st.text_input("Nome:*", 'Nome Completo', key='nome_pf')
        with coluna2:
            apelido_pf = st.text_input("Apelido:", '', key='apelido_pf' )
        with coluna3:
            sexo = st.selectbox("Gênero:*", ['Prefiro não dizer', 'Masculino','Feminino'], index=0)
        with coluna4:
            cpf_pf = st.text_input("CPF:*", '', key= 'cpf_pf', help="Ex.: 000.000.000-00")
        with coluna5:
            rg_pf = st.text_input("RG:*", '', key= 'rg_pf')

        coluna1, coluna2, coluna3 = st.columns([1,2,2])
        with coluna1:
            data_nasc_pf = st.date_input("Data de Nasc.:*", key="date_nasc_input", value=default_date)
        with coluna2:
            coluna2_01, coluna2_02 = st.columns(2)
            with coluna2_01:
                tel_01_pf = st.text_input("Telefone:", '', key = 'tel_01_pf', help="Ex.: (61) 3303-4671")
            with coluna2_02:
                tel_02_pf = st.text_input("Celular:", '', key = 'tel_02_pf', help="Ex.: (61) 9.3303-4671")
        with coluna3:
            email_pf = st.text_input("E-mail:*", key = 'email_pf', help="rodolfoterratechnology@gmail.com")

        coluna1, coluna2, coluna3, coluna4, coluna5 = st.columns([1,4,1,3,1])
        with coluna1:
            cep_pf = st.text_input("CEP:*", '', key= 'cep_pf')
        with coluna2:
            end_pf = st.text_input("Endereço:*", '', key= 'end_pf')
        with coluna3:
            compl_pf = st.text_input("Complemento:", '', key = 'compl_pf')
        with coluna4:
            cidade_pf = st.text_input("Cidade:*", '', key = 'cid_pf')
        with coluna5:
            uf_pf = st.selectbox("UF:*", ufs, index=ufs.index('SP'), key = "uf_pf")

        coluna3, coluna1, coluna2, coluna4 = st.columns(4)
        with coluna1:
            # Adicionando o botão sem usar on_click
            if st.button('✔️ Cadastrar uma nova Pessoa Física.'):
                if(nome_pf == "Nome Completo"):
                    st.warning("❗ Escreva o nome completo da Pessoa Física")
                else:
                    mensagem_sucesso('cadastro_pf', option = 'Adicionar')
            
            
        with coluna2:
            # Adicionando o botão sem usar on_click
            if st.button('❌ Excluir uma Pessoa Física existente.'):        
                if(razao_social == "Nome Completo"):
                    st.warning("❗ Escreva o nome completo da Pessoa Física")
                else:
                    mensagem_sucesso('cadastro_pf', option = 'Excluir')
    st.markdown("___")
    st.markdown('**Obs:** Os Campos que possui **\*** , são **CAMPOS OBRIGATÓRIOS** a serem preenchidos.')

with aba2:
    df_pj = pd.DataFrame.from_dict(supabase.table('cadastro_pj').select('*').execute().data)
    nome_colunas = {"razao_social": 'Razao Social',
                    "cnpj":'CNPJ',
                    "insc_estadual":'Inscrição Municipal',
                    "fundado": 'Data de Fundação',
                    "tel_01_pj":'Telefone Comercial',
                    "cel_02_pj":'Celular',
                    "zap": 'Whats app',
                    "email": 'E-mail',
                    "cep_pj":'CEP',
                    "end_pj":"Endereço",
                    "compl_pj":'Complemento',
                    "cidade_pj":"Cidade",
                    "uf_pj": 'UF',
                    "especialidade": 'Especialidade'
    }
    df_pj = df_pj.rename(columns=nome_colunas)
    nome_colunas = df_pj.columns.tolist()
    colunas_indesejadas = ['id', 'created_at']
    nome_colunas = [coluna for coluna in nome_colunas if coluna not in colunas_indesejadas]
    st.title("Pessoas Jurídica:")

    
    with st.expander("Colunas"):
        selecionar_colunas = st.multiselect('Selecione as Colunas:',
                                    nome_colunas,
                                    ['Razao Social','CNPJ','Telefone Comercial','Celular','E-mail','Especialidade'])
    df_pj = df_pj[selecionar_colunas]
    width = 800
    st.markdown(
            f'<div style="margin:auto; width:{width}px; ">'
            f'{df_pj.to_html(classes="dataframe")}'
            '</div>',
            unsafe_allow_html=True
        )


with aba3:
    df_pf = pd.DataFrame.from_dict(supabase.table('cadastro_pf').select('*').execute().data)
    nome_colunas = {"razao_social":'Empresa', 
                    "nome_pf": 'Nome',
                    "apelido_pf":'Apelido',
                    "sexo": 'Sexo',
                    "cpf_pf": 'CPF',
                    'rg_pf': "RG",
                    'data_nasc_pf': 'Data de Nascimento',
                    "tel_01_pf":'Telefone 01',
                    "tel_02_pf":'Celular',
                    "email_pf": "E-mail",
                    "cep_pf":'CEP', 
                    "end_pf":'Endereço', 
                    "compl_pf":'Complemento',
                    "cidade_pf":'Cidade',
                    "uf_pf": 'Estado'}
    df_pf = df_pf.rename(columns=nome_colunas)
    nome_colunas = df_pf.columns.tolist()
    colunas_indesejadas = ['id', 'created_at']
    nome_colunas = [coluna for coluna in nome_colunas if coluna not in colunas_indesejadas]
    st.title("Pessoas Físicas:")

    
    with st.expander("Colunas"):
        selecionar_colunas = st.multiselect('Selecione as Colunas:',
                                    nome_colunas,
                                    ['Empresa','Nome','Celular','E-mail'])
    df_pf = df_pf[selecionar_colunas]
    width = 800
    st.markdown(
            f'<div style="margin:auto; width:{width}px; ">'
            f'{df_pf.to_html(classes="dataframe")}'
            '</div>',
            unsafe_allow_html=True
        )



