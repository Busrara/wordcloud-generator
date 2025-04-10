# -*- coding: utf-8 -*-

import gradio as gr
from wordcloud_generator import WordCloudGenerator

def create_wordcloud_app():
    """Create and launch the Gradio application"""
    generator = WordCloudGenerator()

    with gr.Blocks(title="Word Cloud Generator") as app:
        gr.Markdown("# 🌥️ Word Cloud Generator")

        with gr.Row():
            with gr.Column():
                text_input = gr.TextArea(label="Input Text", placeholder="Paste your text here to generate a word cloud", lines=10)

                with gr.Row():
                    shape = gr.Radio(["rectangle", "circle"], value="rectangle", label="Shape")
                    palette = gr.Dropdown(["viridis", "plasma", "magma", "inferno", "Blues", "Greens", "Reds", "YlOrBr"], value="viridis", label="Color Palette")
                    bg_color = gr.Radio(["white", "black"], value="white", label="Background")

                stopwords = gr.TextArea(label="Exclude Words (comma-separated)", placeholder="word1, word2, word3", lines=2)

                btn = gr.Button("Generate Word Cloud", variant="primary")

            with gr.Column():
                output = gr.Image(label="Generated Word Cloud")

                gr.Markdown("""
                ### Usage Instructions
                1. Paste your text in the input area
                2. Adjust the shape, color palette, and background options as desired
                3. Optionally specify words to exclude (comma-separated)
                4. Click "Generate Word Cloud" button
                The most frequently occurring words will appear larger in the word cloud.
                """)

        def generate_cloud(text, shape, palette, bg, stopwords_text):
            generator.add_stopwords(stopwords_text)
            return generator.generate(text, shape, palette, bg)

        btn.click(fn=generate_cloud, inputs=[text_input, shape, palette, bg_color, stopwords], outputs=output)

    app.launch(share=True)

if __name__ == "__main__":
    print("Starting Word Cloud Generator application...")
    create_wordcloud_app()
