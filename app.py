import streamlit as st
import os
import openai
import google.generativeai as genai

# Get Google API key from environment variable
GOOGLE_API_KEY = "AIzaSyDrIV31lOfDBc4cH6_gNz7NLagwRQh15v0"
api_key = os.getenv("AIzaSyDrIV31lOfDBc4cH6_gNz7NLagwRQh15v0", GOOGLE_API_KEY)

st.set_page_config(page_title="BizGen")

# Function to map model roles to Streamlit roles
def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

# Initialize chat history in session state
if "chat" not in st.session_state:
    st.session_state.chat = openai.ChatCompletion.create(
        model="your_openai_model_name_here"
    )

st.title("BizGen (Business Idea Generator)")

# Display additional information
st.subheader("Final Project in CCS 229 - Intelligent Systems")
st.subheader("Ma. April G. Suarnaba - BSCS 3-B AI")
st.write(
    "BizGen or (Business Idea Generator) is an innovative platform designed to revolutionize the way entrepreneurs and business enthusiasts generate and refine business ideas."
)

# Display chat messages from history above current input box
for message in st.session_state.chat.messages:
    with st.beta_container():  # Container for better layout
        st.markdown(f"**{message.get('role', 'User').capitalize()}**: {message['content']}")

# Accept user's next message, add to context, resubmit context to OpenAI
if prompt := st.text_input("Ask me any questions about Business!"):
    # Send user entry to OpenAI and read the response
    response = st.session_state.chat.send_message(prompt)

    # Display assistant's response
    with st.beta_container():  # Container for better layout
        st.markdown(f"**Assistant**: {response['choices'][0]['message']['content']}")
