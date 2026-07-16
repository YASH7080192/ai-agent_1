import os
import streamlit as st
from agent import Agent

st.set_page_config(
    page_title="AI Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Agent")
st.caption("ChatGPT Style AI Agent")

# -------------------------------
# Initialize
# -------------------------------
if "agent" not in st.session_state:
    st.session_state.agent = Agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Show Old Messages
# -------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and message.get("tool") == "qrcode"
            and message.get("qr_path")
            and os.path.exists(message["qr_path"])
        ):
            st.image(
                message["qr_path"],
                caption="Generated QR Code",
                width=250
            )

# -------------------------------
# User Input
# -------------------------------
prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):

        response = st.session_state.agent.run(prompt)

    # -----------------------------------------
    # If Agent returned dictionary
    # -----------------------------------------
    if isinstance(response, dict):

        assistant_text = response["response"]

        assistant_message = {
            "role": "assistant",
            "content": assistant_text,
            "tool": response.get("tool"),
            "qr_path": response.get("qr_path")
        }

        st.session_state.messages.append(assistant_message)

        with st.chat_message("assistant"):

            st.markdown(assistant_text)

            if (
                response.get("tool") == "qrcode"
                and response.get("qr_path")
                and os.path.exists(response["qr_path"])
            ):
                st.image(
                    response["qr_path"],
                    caption="Generated QR Code",
                    width=250
                )

    # -----------------------------------------
    # Normal Response
    # -----------------------------------------
    else:

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        with st.chat_message("assistant"):
            st.markdown(response)