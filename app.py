import gradio as gr
from model import generate_image

def create_app():
    with gr.Blocks() as demo:
        gr.Markdown("## 🖼️ AI Image Generator using Stable Diffusion")
        prompt = gr.Textbox(label="Enter your prompt", placeholder="e.g., A dragon flying in the sky")
        btn = gr.Button("Generate")
        img = gr.Image(label="Generated Image", interactive=True)
        btn.click(fn=generate_image, inputs=prompt, outputs=img)
    return demo

demo = create_app()
demo.launch()
