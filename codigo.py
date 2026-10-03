import streamlit as st
from openai import OpenAI
modelo_ia = OpenAI(api_key= '',
base_url = 'https://generativelanguage.googleapis.com/v1beta/openai')
st.write('## chat bot com ia')
if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = []
mensagem_usuario = st.chat_input('escreva sua mensagem aqui')
for mensagem in st.session_state['lista_mensagens'] :
    quem_envio = mensagem['role']
    texto_mensagem = mensagem['content']
    st.chat_message(quem_envio).write(texto_mensagem)
if mensagem_usuario:
    st.chat_message('user').write(mensagem_usuario)
    mensagem1 = {'role': 'user', 'content': mensagem_usuario}
    st.session_state['lista_mensagens'].append(mensagem1)
    resposta_modelo = modelo_ia.chat.completions.create(
    messages=st.session_state['lista_mensagens'],
    model='gemini-flash-latest'   
    )
    resposta_ia= resposta_modelo.choices[0].message.content
    st.chat_message('assistant').write(resposta_ia)
    mensagem2 = {'role': 'assistant', 'content': resposta_ia}
    st.session_state['lista_mensagens'].append(mensagem2)



