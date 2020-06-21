import streamlit as st

def main():
    st.title('Hello world!')
    st.header('This is a header')
    st.subheader('This is a subheader')
    st.text('Keep calm and listen: Janeret - Atlas')
    #st.image('logo.png')
    st.audio('3 - Atlas.flac')
    #st.video('video.mov')
    botao = st.button('Botão')
    if botao:
        st.markdown('Clicado')
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('Clicado')
    radio = st.radio('Escolha as opções:', ('Opção 1', 'Opção 2'))
    if radio == 'Opção 1':
        st.markdown('Opção 1')
    if radio == 'Opção 2':
        st.markdown('Opção 2')
    st.markdown('Selectbox')
    select = st.selectbox('Chose opt:', ('Opt1', 'Opt2'))
    if select == 'Opt1':
        st.markdown('Opt1')
    if select == 'Opt2':
        st.markdown('Opt2')
    multi = st.multiselect('Chose: ', ('Opt1', 'Opt2'))
    if multi == 'Opt1':
        st.markdown('Opt1')
    if multi == 'Opt2':
        st.markdown('Opt2')
    st.markdown('File uploader')
    file = st.file_uploader('Chose your file', type = 'csv')
    if file is not None:
        st.markdown('Não está vazio.')

if __name__ == '__main__':
    main()