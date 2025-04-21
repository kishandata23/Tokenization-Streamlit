import streamlit as st
import tiktoken
st.title("Tokenization")

st.text('')




st.markdown('''Check out my blog about Tokenization
[link]()
''')




tab1,  tab3 = st.tabs(["Open-AI",  "Plain"])

with tab1:
    st.write("🤖 Open AI library tiktoken")
    # api_key = st.text_input("Enter your API Key")
    # st.success("We don't store your API keys or any personal information")

    my_model = st.selectbox('Select your model',['gpt-4o','text-embedding-3-small','gpt-4-0314','gpt-3.5-turbo'])
    if my_model:
        encoder = tiktoken.encoding_for_model(my_model)
    else:
        encoder = tiktoken.encoding_for_model('gpt-4o')
    input_text = st.text_input('Enter your text :')
    tokens = encoder.encode(input_text)
    output_text = st.text(tokens)





with tab3:
    st.write("🤖 Simple alphabet ")

    input_text = st.text_input('')
    text = input_text.upper()
    result = [ord(char) - 64 for char in text if char.isalpha()]
    st.text(result)