import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the conversation template
template = """
Answer the following question.
Here is the conversation history:
{context}

Question: {question}
Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Function to handle conversation
def handle_convo(context, question):
    result = chain.invoke({"context": context, "question": question})
    return result

# Streamlit App
st.title("AI Chatbot")

if 'context' not in st.session_state:
    st.session_state.context = ""  # Store full chat context
if 'conversation' not in st.session_state:
    st.session_state.conversation = []  # Store formatted chat messages


# Input field for user input
question = st.chat_input("Type your message here...")  # Get user input dynamically

# Handle "Send" button logic
if question:
    # Call the language model
    response = handle_convo(st.session_state.context, question)
    # Update session state
    st.session_state.context += f"\nYou: {question}\nAI: {response}"
    st.session_state.conversation.append(("You", question))
    st.session_state.conversation.append(("AI", response))

# Display chat history
st.subheader("Chat History")
for role, message in st.session_state.conversation:
    if role == "You":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)
