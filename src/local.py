import openai

def read_knowledge_base(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        knowledge_base = file.read()
    return knowledge_base

def gpt_35_api_stream(messages: list, knowledge_base_file: str):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
        knowledge_base_file (str): 知识库文件路径
        api_key (str): OpenAI API 密钥

    Returns:
        tuple: (results, error_desc)
    """
    try:
        knowledge_base = read_knowledge_base(knowledge_base_file)
        messages_copy = messages.copy()

        # 将知识库作为第一条消息添加到对话中
        messages_copy.insert(0, {'role': 'system', 'content': knowledge_base})

        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages_copy,
            stream=True,
        )

        completion = {'role': '', 'content': ''}
        for event in response:
            if event['choices'][0]['finish_reason'] == 'stop':
                print(f'收到的完成数据: {completion}')
                break
            for delta_k, delta_v in event['choices'][0]['delta'].items():
                print(f'流响应数据: {delta_k} = {delta_v}')
                completion[delta_k] += delta_v

        messages.append(completion)  # 直接在传入参数 messages 中追加消息
        return (True, '')
    except Exception as err:
        return (False, f'OpenAI API 异常: {err}')
