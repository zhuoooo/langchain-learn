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

from local import gpt_35_api_stream

if __name__ == '__main__':
    messages = [{'role': 'user','content': '鲁迅和周树人的关系'},]
    print(gpt_35_api_stream(messages))
    print(messages)