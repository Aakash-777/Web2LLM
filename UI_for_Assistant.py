import streamlit as st
import ollama

st.set_page_config(page_title="Local Chatbot", page_icon="💬")
st.title("💬 Local Chatbot using Ollama")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Build full conversation history for context
    history = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        for chunk in ollama.chat(
            model="llama3.2",
            messages=history,
            stream=True
        ):
            full_response += chunk["message"]["content"]
            response_placeholder.markdown(full_response + "▌")

        response_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
