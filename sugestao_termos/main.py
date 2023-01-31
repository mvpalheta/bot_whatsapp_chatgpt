#Carregando os pacotes neccessário juntamente com o arquivo "resouces.py" que contém algumas funções a serem utilizadas
from datetime import datetime
from resources import *
import streamlit as st
import pandas as pd

# Setando algumas configurações para o app do formulário
st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title='Formulário para sugestões de termos')

# Definindo, via HTML, algumas outras configurações para a aplicação
st.markdown(""" <style type="text/css"> 
div.streamlit-expanderHeader {
  display:none;
}
</style>""", unsafe_allow_html=True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.markdown(""" <style type="text/css"> 
div.css-sg054d {
  display:none;
}
</style>""", unsafe_allow_html=True)

########################################## Formulário para receber sugestões de termos ##################################################
def main():
    # Definindo uma caixa de seleção na sidebar com um valor default (none) e uma alias (key='page_nav')
    st.sidebar.selectbox('bla', ['none'], key='page_nav')
    # Se a caixa de seleção na sidebar estiver com o seu valor default
    if st.session_state.page_nav == 'none':
    # Definindo uma função que vai mostrar a msg de confirmação de envio realizado e alterar o valor da caixa de seleção na sidebar 
    # para "confirma_envio_form"
        def send_form_success():
            st.session_state.page_nav = "confirma_envio_form"
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(' ')
            with col2:
                with st.expander('', expanded=True):
                    st.success('Cadastro realizado com sucesso!!!')                  
            with col3:
                    st.write(' ')
        # Criando um dicionário para guardar os termos sugeridos
        dict_termos_sugeridos = {"termo":[], "dh_sugestao":[]}
        # Criando o formulário
        st.subheader('Sugestão de termos')
        st.write("Preencha o campo abaixo para sugerir um novo termo a ser adicionado. Caso queira inserir mais de um termo, favor \
            separar por ponto e vírgula ( ; ).")
        termos_sugeridos = st.text_input("Sugestões de termos")
        # Guardando os termos sugeridos em uma lista
        lista_termos_sugeridos = termos_sugeridos.split (";")

        # Definindo uma função que vai enviar os termos sugeridos no formulário para um bucket no S3
        def enviar_form():
            # Se formulário não estiver preenchido, solicita o preenchimento
            if termos_sugeridos.replace(' ', '') == '':
                st.error("Por favor, sugira ao menos um termo")
            # Adiciona os termos sugeridos ao dicionário criado anteriormente, com data e hora da sugestão, transforma em um dataframe 
            # e a função "save2s3" salva no bucket 'botwhatsapp' como um arquivo CSV
            else:
                dict_termos_sugeridos["termo"] += lista_termos_sugeridos
                dh_sugestao = []
                for i in range(len(lista_termos_sugeridos)):
                    dh_sugestao.append(datetime.now())
                dict_termos_sugeridos["dh_sugestao"] += dh_sugestao
                df_termos_sugeridos = pd.DataFrame.from_dict(dict_termos_sugeridos)
                filename = 'novas_sugestoes_termos/termos_sugeridos_em_' + str(datetime.now()).replace(':', '-').replace('.', '-') + '.csv'
                status = save2s3(df_termos_sugeridos, 'botwhatsapp', filename)
                # Se o envio ocorreu com sucesso chama a função "send_form_success", com a msg confirmando o envio e alterando o valor da caixa de seleção na sidebar 
                # para "confirma_envio_form"
                if status == 200:
                    send_form_success()
                else:
                    st.error('Ocorreu algum problema no envio. Por favor, tente novamente.')      
        col1, col2 = st.columns([1,10])
        with col1:
                # Botão de enviar, quando for clicado chama a função acima (enviar_form)
                st.button('Enviar', on_click=enviar_form)
        with col2:
                st.write("")
        st.write("**Críticas e/ou sugestões: mvpalheta@gmail.com**")
    ######################################## Página de confirmação de envio dos dados para notificação ####################################
    #Se o valor valor da caixa de seleção na sidebar for alterado para "confirma_envio_form", quer dizer que o envio ocorreu com sucesso. 
    # Então, cria-se uma uma página em branco
    if st.session_state.page_nav == "confirma_envio_form":
        st.write("")
        


if __name__ == "__main__":
    main()