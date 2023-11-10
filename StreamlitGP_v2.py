# Import the module
from openai import OpenAI
import streamlit as st

client = OpenAI()

st.title("Sassy Chatbot:face_with_rolling_eyes:")

st.sidebar.header("Options")
max_tokens = st.sidebar.slider("Max Tokens", 1, 250, 100)
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
model = st.sidebar.selectbox("Model", ("gpt-3.5-turbo","Other"))
system_message_type = st.sidebar.selectbox("System Message",("Sassy Assistant", "Bored Assistant", "Angry Assistant", "Custom"))


# Define the system message
if system_message_type == "Sassy Assistant":
    system_message = "You are a sassy assistant that is fed up with answering questions."
elif system_message_type == "Bored Assistant":
    system_message = "You are a bored assistant that does the bare minimum."
elif system_message_type == "Angry Assistant":
    system_message = "You are an angry assistant that likes yelling in all caps."
elif system_message_type == "Custom":
    system_message = st.sidebar.text_area("Custom System Message", "Enter your custom system message here.")
else:
    system_message = "You are a helpful assistant."

if st.sidebar.button("Apply Settings"):
    st.session_state.messages = []
    st.session_state["messages"] = [{"role": "system", "content": system_message}]
    st.rerun()
st.sidebar.write("Warning: Applying new settings will clear the chat history.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": system_message}]

for msg in st.session_state.messages:
    if msg["role"] == "user" or msg["role"] == "assistant":
        st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
        model=model,
        messages=st.session_state.messages,
        temperature=temperature,
        max_tokens=max_tokens)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    if len(st.session_state.messages) > 20:
        st.session_state.messages = st.session_state.messages[-20:]

