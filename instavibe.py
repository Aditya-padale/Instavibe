import streamlit as st
import os
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)


prompt = PromptTemplate(
    input_variables=["traits", "style"],
    template="Make a short bio (under 150 characters) for a person who is {traits}. Style: {style}."
)

chain = LLMChain(llm=llm, prompt=prompt)

st.title("Instagram Bio App")

traits = st.text_input("type some traits here:")
style = st.text_input("bio style:")

if st.button("generate bio"):
    if traits != "":
        result = chain.run(traits=traits, style=style)
        st.write("Bio is below:")
        st.write(result)
    else:
        st.write("you didnt type anything")