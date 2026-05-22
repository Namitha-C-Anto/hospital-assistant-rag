import streamlit as st 

def get_chat_history():

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

    return st.session_state.chat_history

def save_chat(question, answer):

    st.session_state.chat_history.append(
        {
            "question": question,
            "answer": answer
        }
    )