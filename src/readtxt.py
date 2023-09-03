from bs4 import BeautifulSoup
import langchain
import markdown
from sklearn.feature_extraction.text import TfidfVectorizer

def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    html_content = markdown.markdown(content)
    text_content = ''.join(BeautifulSoup(html_content, "html.parser").findAll(text=True))
    return text_content

markdown_files = ["./README.md"]  # 替换为您自己的 Markdown 文件路径
documents = []

for file in markdown_files:
    text_content = read_md_file(file)
    documents.append(text_content)

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents)

print(vectors)
