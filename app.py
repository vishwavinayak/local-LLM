from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the following question.
Here is the conversation history {context}

Question: {question}
Answer:
"""

model = OllamaLLM(model = "llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_convo():
    context = ""
    print("Welcome to AI chatbot, type 'exit' to quit")
    while True:
        question = input("You: ")
        if question.lower() == "exit":
            break
        result = chain.invoke({"context":context,"question": question})
        print("AI: ", result)
        context += f"\nYou: {question}\nAI: {result}"

if __name__ == "__main__":
    handle_convo()
