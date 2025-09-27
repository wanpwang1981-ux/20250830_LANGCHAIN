## 從playground COPY 介面測試
import gradio as gr


def greet(name):
    return "Hello " + name + "!"


demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")
# share=True可以分享外網
if __name__ == "__main__":
    demo.launch(share=True)
