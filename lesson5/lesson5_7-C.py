from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
import gradio as gr

# 初始化模型
model = OllamaLLM(model="llama3.2:latest")

# 建立多變數的翻譯模板
complex_template = """
你是一位專業的{target_language}翻譯家，專精於{domain}領域。
請將以下{source_language}文本翻譯成{target_language}，並確保：
1. 保持原文的語氣和風格
2. 使用專業術語
3. 符合{target_language}的語言習慣

{source_language}文本：{text}
{target_language}翻譯：
"""

chat_prompt_template = ChatPromptTemplate.from_template(complex_template)

# 核心翻譯函式
def translate(text, source_language, target_language, domain):
    prompt = chat_prompt_template.format(
        target_language=target_language,
        source_language=source_language,
        domain=domain,
        text=text
    )
    response = model.invoke(prompt)
    return response

# Gradio 介面
iface = gr.Interface(
    fn=translate,
    inputs=[
        gr.Textbox(label="原文（輸入要翻譯的內容）", lines=5),
        gr.Dropdown(choices=["英文", "繁體中文", "日文", "韓文"], value="英文", label="來源語言"),
        gr.Dropdown(choices=["繁體中文", "英文", "日文", "韓文"], value="繁體中文", label="目標語言"),
        gr.Dropdown(choices=["商業", "科技", "醫療", "旅遊", "文學"], value="商業", label="領域")
    ],
    outputs=gr.Textbox(label="翻譯結果（專業翻譯與優化）"),
    title="多變數 LLM 專業自動翻譯"
)

iface.launch()  # 打開網頁本地介面
