# MEU PRIMEIRO WEB APP
import streamlit as st

form = st.form("formHD")
nome = st.text_input("Digite seu nome:")
email = st.text_input("Digite seu e-mail:")
prioridade = st.selectbox("Prioridade: ",("Baixa", "Medio", "Alta", "*Critico*"))
assunto = st.text_input("Assunto: ")
mensagem = st.text_input("Messagem: ")

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

#problema = st.selectbox("Qual o problema apresentado?",("Sem Internet", "Alteração de Senha", "Outros"))
botao = st.button("Enviar")
