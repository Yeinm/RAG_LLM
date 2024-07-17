import os
from langchain_community.llms import QianfanLLMEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from project2.API_Config import *
os.environ["QIANFAN_AK"] = QIANFAN_AK
os.environ["QIANFAN_SK"] = QIANFAN_SK

#1. 定义模板
template = "我的邻居姓{lastname}，他生了个儿子，给他儿子起个名字"
prompt = PromptTemplate(input_variables=["lastname"], template=template)

# 2.实例化模型
llm = QianfanLLMEndpoint()

# 3.构造CHain
chain = LLMChain(llm=llm, prompt=prompt)

# 4.执行Chain
result = chain.run("王")
print(f'result-->{result}')