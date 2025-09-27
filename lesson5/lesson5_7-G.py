import gradio as gr
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from typing import Literal

# 檢查 ollama 服務是否正在運行，否則此處會出錯。
# 假設 Ollama 服務已經在本機啟動
try:
    # --- 1. 定義 LangChain 核心組件 ---
    # 載入模型 (請確認您的 Ollama 服務中有 llama3.2:latest)
    model = OllamaLLM(model="llama3.2:latest")

    # 建立多變數的翻譯模板
    COMPLEX_TEMPLATE = """
    你是一位專業的{target_language}翻譯家，專精於{domain}領域。
    請將以下{source_language}文本翻譯成{target_language}，並確保：
    1. 保持原文的語氣和風格
    2. 使用專業術語
    3. 符合{target_language}的語言習慣

    {source_language}文本：{text}
    {target_language}翻譯：
    """
    chat_prompt_template = ChatPromptTemplate.from_template(COMPLEX_TEMPLATE)

except Exception as e:
    print(f"初始化模型或 LangChain 發生錯誤，請檢查 Ollama 服務是否運行並模型名稱是否正確: {e}")
    # 在 Gradio 介面中回報錯誤，而不是直接中斷程式
    model = None 


# --- 2. 核心翻譯函數 (供 Gradio 呼叫) ---

def translate_text(
    target_language: str, 
    source_language: str, 
    domain: str, 
    text: str
) -> str:
    """
    接收使用者輸入的參數，格式化 Prompt 並呼叫 Ollama 模型進行翻譯。
    
    Args:
        target_language: 目標語言
        source_language: 來源語言
        domain: 專業領域
        text: 待翻譯的文本
        
    Returns:
        模型的翻譯結果，如果初始化失敗則返回錯誤訊息。
    """
    if model is None:
        return "❌ 翻譯模型初始化失敗。請檢查您的 Ollama 服務是否正在運行，且 'llama3.2:latest' 模型已下載並可用。"

    if not text.strip():
        return "請輸入您想要翻譯的文本！"
    
    # 格式化 Prompt
    formatted_prompt = chat_prompt_template.format(
        target_language=target_language,
        source_language=source_language,
        domain=domain,
        text=text
    )
    
    print(f"--- 呼叫模型，領域: {domain}, 文本長度: {len(text)} ---") # log 紀錄

    try:
        # 呼叫模型取得回應
        response = model.invoke(formatted_prompt)
        return response.strip()
    except Exception as e:
        return f"🚨 模型呼叫失敗: {e}"


# --- 3. 建立 Gradio 介面 ---

# 設定下拉選單的預設選項
DOMAIN_CHOICES = ["商業", "科技", "法律", "醫學", "文學", "一般"]
LANGUAGE_CHOICES = ["繁體中文", "英文", "日文", "西班牙文", "法文"]

with gr.Blocks(title="LangChain x Gradio 專業翻譯機") as demo:
    gr.Markdown(
        """
        # 🤖 LangChain/Ollama 專業翻譯機
        此工具使用 **Ollama/llama3.2:latest** 結合 **LangChain ChatPromptTemplate** 進行**多變數**翻譯。
        您可以指定翻譯的**目標語言**、**來源語言**和**專業領域**。
        """
    )
    
    with gr.Row():
        # 輸入區塊 (左側)
        with gr.Column(scale=1):
            target_lang_input = gr.Dropdown(
                label="🎯 目標語言 (Target Language)",
                choices=LANGUAGE_CHOICES,
                value="繁體中文",
                allow_custom_value=True,
                interactive=True
            )
            
            source_lang_input = gr.Dropdown(
                label="🌐 來源語言 (Source Language)",
                choices=LANGUAGE_CHOICES,
                value="英文",
                allow_custom_value=True,
                interactive=True
            )
            
            domain_input = gr.Dropdown(
                label="📚 專業領域 (Domain)",
                choices=DOMAIN_CHOICES,
                value="商業",
                allow_custom_value=True,
                interactive=True
            )
            
            # 翻譯按鈕
            translate_button = gr.Button("🚀 開始翻譯", variant="primary")

        # 文本輸入區塊 (中間)
        with gr.Column(scale=2):
            text_input = gr.Textbox(
                label="✍️ 待翻譯文本 (Source Text)",
                lines=10,
                placeholder="請輸入您想翻譯的文本...",
                value="The quarterly revenue increased by 15% compared to last year."
            )
        
        # 輸出區塊 (右側)
        with gr.Column(scale=2):
            translation_output = gr.Textbox(
                label="✅ 翻譯結果 (Target Translation)",
                lines=10,
                interactive=False # 輸出結果不可編輯
            )

    # 設定按鈕點擊事件，將輸入傳給 translate_text 函數，並將結果輸出到 translation_output
    translate_button.click(
        fn=translate_text,
        inputs=[
            target_lang_input, 
            source_lang_input, 
            domain_input, 
            text_input
        ],
        outputs=translation_output
    )

# 啟動 Gradio 應用
print("\n🔥 Gradio 介面啟動中... 請開啟瀏覽器前往 http://127.0.0.1:7860")
if __name__ == "__main__":
    demo.launch()