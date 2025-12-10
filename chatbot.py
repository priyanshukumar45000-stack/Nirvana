import streamlit as st
from openai import OpenAI
import os


client = OpenAI(api_key="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")

st.set_page_config(page_title="ChatBot", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
            
    .main-title {
        background:rgba(128, 128, 128, 0.7);
        color: white;
        text-align: center;
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 20px;
        font-size: 38px;
    }
    .ChatMessage {
        border-radius: 18px;
        padding: 12px 16px;
        margin: 8px 0;
        max-width: 75%;
        word-wrap: break-word;
        font-size: 15px;
        line-height: 1.4;
    }
    .stChatMessage.user {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        color: white;
        margin-left: auto;
    }
    .stChatMessage.assistant {
        background: #f1f3f4;
        color: #333;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🤖 My Chatbot</div>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def get_response(user_inp):
 lower_inp=user_inp.lower()
 try:
       response = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                *st.session_state.chat_history,  
                {"role": "user", "content": user_inp},
            ],
        )
       return response.choices[0].message.content
 except Exception:
        return f"⚠️ something went wrong"

user_inp = st.chat_input("How can i help you?")

if user_inp:
    st.session_state.chat_history.append({"role": "user","content" :user_inp})
    response = get_response(user_inp)
    st.session_state.chat_history.append({"role":"assistant","content" :response})

for msg in st.session_state.chat_history:

    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])