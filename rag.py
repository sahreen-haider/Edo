from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import (StuffDocumentsChain, LLMChain, ConversationalRetrievalChain)
from langchain_core.prompts import PromptTemplate


loader = TextLoader(file_path="scalexi.txt", encoding='utf-8')
data = loader.load()

text_split = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
data = text_split.split_documents(data)

embedding = OpenAIEmbeddings()

vector_store = FAISS.from_documents(data, embedding = embedding)

llm = ChatOpenAI(temperature=0.1)

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(),
    memory=memory
)