import os
from langchain_community.embeddings import QianfanEmbeddingsEndpoint
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter

from project2.API_Config import *
os.environ["QIANFAN_AK"] = QIANFAN_AK
os.environ["QIANFAN_SK"] = QIANFAN_SK

# 1.加载文档
loader = TextLoader('./pku.txt', encoding='utf8')
docments = loader.load()
# print(f'docments-->{docments}')
# print(type(docments))

# 2.切分文档
text_spliter = CharacterTextSplitter(chunk_size=100,
                                     chunk_overlap=5)
texts = text_spliter.split_documents(docments)
# print(texts)
# print(len(texts))
# 3. 实例化embedding模型
embed = QianfanEmbeddingsEndpoint()
db = FAISS.from_documents(texts, embed)
retriever = db.as_retriever(search_kwargs={"k": 1})
result = retriever.get_relevant_documents("北京大学什么时候成立的？")
print(result)