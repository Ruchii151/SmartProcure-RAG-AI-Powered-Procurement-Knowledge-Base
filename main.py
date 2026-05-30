# load required libraries
import streamlit as st
import os
import pandas as pd
import time

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import OllamaEmbeddings

from langchain_community.document_loaders import PyPDFLoader

from langchain_core.documents import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_chroma import Chroma

from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from langchain_classic.chains import create_retrieval_chain


# load environment variables
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# User Interface
st.title("SmartProcure-RAG")

st.write("Ask questions about suppliers, pricing, contracts, certifications and procurement documents.")

# all documents folder
DATA_FOLDER = "supplier_documents"


# building vector store 

if "vectors" not in st.session_state:

    with st.spinner("Building Knowledge Base..."):

        all_docs = []

        # loading pdf (pypdf loader) 
        for file in os.listdir(DATA_FOLDER):

            if file.endswith(".pdf"):

                loader = PyPDFLoader(os.path.join(DATA_FOLDER, file))

                docs = loader.load()

                for doc in docs:
                    doc.metadata["source"] = file

                all_docs.extend(docs)

        # Loading excel 

        for file in os.listdir(DATA_FOLDER):

            if file.endswith(".xlsx"):

                try:

                    excel_path = os.path.join(DATA_FOLDER, file)

                    excel_sheets = pd.read_excel(
                        excel_path,
                        sheet_name=None,
                        engine="openpyxl"
                    )

                    for sheet_name, df in excel_sheets.items():

                        df = df.dropna(how="all")
                        df = df.fillna("")

                        for index, row in df.iterrows():

                            content = " | ".join(
                                [
                                    f"{col}:{str(row[col])}"
                                    for col in df.columns
                                    if str(row[col]).strip() != ""
                                ]
                            )

                            full_content = (
                                f"File: {file} | "
                                f"Sheet: {sheet_name} | "
                                f"Row: {index + 1}\n"
                                f"{content}"
                            )

                            all_docs.append(
                                Document(
                                    page_content=full_content,
                                    metadata={
                                        "source": file,
                                        "sheet": sheet_name,
                                        "row": index + 1,
                                        "type": "excel"
                                    }
                                )
                            )

                except Exception as e:
                    st.error(f"Error loading Excel {file}: {e}")



        # Splitting documents into chunks (text splitter)   

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)

        final_documents = splitter.split_documents(all_docs)

        # Embeddings (ollama embeddings)

        embeddings = OllamaEmbeddings(model="nomic-embed-text")

        # Vector Database (chroma)
        
        st.session_state.vectors = (Chroma.from_documents(final_documents,embeddings))

# Model (gemini 2.5 flash)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)

# prompt template

procurement_prompt = ChatPromptTemplate.from_template(
"""
You are an expert AI Procurement Assistant.

Use ONLY the supplied context.

Context:
{context}

Question:
{input}

Instructions:

- Answer only from the supplied documents.
- Focus on supplier information.
- Mention pricing, payment terms,
  lead times, certifications,
  contracts, risks and performance
  whenever relevant.

- If information is unavailable say:

"The supplier documents do not contain this information."

Answer:
"""
)

# CHAIN
document_chain = create_stuff_documents_chain(llm,procurement_prompt)

retriever = st.session_state.vectors.as_retriever(search_kwargs={"k": 5})

retrieval_chain = create_retrieval_chain(retriever,document_chain)

# UI for asking questions

question = st.text_input("Ask a procurement question")

# Response 

if question:

    start = time.process_time()

    response = retrieval_chain.invoke({"input": question})

    end = time.process_time()

    st.subheader("Answer")

    st.write(response["answer"])

    st.write(f"Response Time: {round(end-start,2)} sec")
    
    with st.expander("Sources Used"):

        sources = set()

        for doc in response["context"]:
            sources.add(doc.metadata.get("source"))

        for source in sources:
            st.write(source)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
