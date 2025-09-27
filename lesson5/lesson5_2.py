from langchain_ollama import ChatOllama
import gradio as gr
from dotenv import load_dotenv
import os

# 載入環境變數（可用 OLLAMA_URL / OLLAMA_MODEL 覆蓋預設）
load_dotenv()


# 使用最原始的呼叫方式：直接以字串 prompt 送到 Ollama
model = ChatOllama(model="gemma3:270m", base_url="http://localhost:11434")


def answer(prompt: str) -> str:
    """最簡單的 wrapper：把 prompt 傳給 model.invoke，回傳文字回應。"""
    if not prompt:
        return ""
    res = model.invoke(prompt)
    return res.content if hasattr(res, "content") else str(res)


# 最小的 Gradio 介面：一個輸入框 + 一個文字輸出
iface = gr.Interface(
    fn=answer,
    inputs=gr.Textbox(lines=3, placeholder="在此輸入問題，按送出..."),
    outputs="text",
    title="Ollama 簡易 Gradio 範例",
    description="示範如何把原先的 Ollama 呼叫整合到 Gradio。可用 OLLAMA_URL/OLLAMA_MODEL 環境變數覆蓋預設。",
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0",share=True)