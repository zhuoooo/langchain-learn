import os
import importlib
import openai

if os.path.exists('config_dev.py'):  # 检查是否存在 config_dev.py 文件
    config_module = importlib.import_module('config_dev')
else:
    config_module = importlib.import_module('config')

# openai.log = "debug"
openai.api_key = config_module.API_KEY
openai.api_base = config_module.API_BASE

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import AgentType

# 加载 OpenAI 模型
llm = OpenAI(temperature=0,max_tokens=2048,openai_api_key=config_module.API_KEY,openai_api_base=config_module.API_BASE) 

 # 加载 serpapi 工具
tools = load_tools(["serpapi"])

# 如果搜索完想再计算一下可以这么写
# tools = load_tools(['serpapi', 'llm-math'], llm=llm)

# 如果搜索完想再让他再用python的print做点简单的计算，可以这样写
# tools=load_tools(["serpapi","python_repl"])

# 工具加载后都需要初始化，verbose 参数为 True，会打印全部的执行详情
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 运行 agent
agent.run("What's the date today? What great events have taken place today in history?")

# from src.local import gpt_35_api_stream

# if __name__ == '__main__':
#     messages = [
#         {'role': 'user', 'content': '印度近期的登月情况'},
#         {'role': 'assistant', 'content': '请问有什么可以帮助您的？'}
#     ]
#     knowledge_base_file = './src/README.md'
#     # messages = [{'role': 'user','content': '鲁迅和周树人的关系'},]
#     # print(gpt_35_api_stream(messages))
#     # print(messages)
#     results, error_desc = gpt_35_api_stream(messages, knowledge_base_file)
#     if results:
#         print('回答生成成功')
#     else:
#         print(f'回答生成失败: {error_desc}')