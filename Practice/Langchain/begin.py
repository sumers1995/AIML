from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore



model = OllamaLLM(model="llama3.2:1b")
query = "How many awards did Hulu won?"
prompt = ChatPromptTemplate.from_template(query)

chain = prompt | model

# result = chain.invoke({"question": query})
# print(result)

file = "Hulu is great. she has already lost 3 kgs. She has won many awards."
combined_text = ""
combined_text += file
text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 200,
    chunk_overlap = 20,
    length_function = len)

finalData = text_splitter.split_text(combined_text)

embeddings = OllamaEmbeddings(model="mxbai-embed-large")
document_search = FAISS.from_texts(finalData, embeddings)

docs = document_search.similarity_search(query=query)

vector_store = InMemoryVectorStore(embedding=embeddings)
vector_store.add_documents()

