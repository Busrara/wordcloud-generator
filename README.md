# wordcloud-generator



A simple and interactive Word Cloud Generator that we can use to create word clouds from our input text. The app offers customization options for word cloud shape, color palette, background color, and the option to exclude specific words.

You can see the image result here: https://github.com/Busrara/wordcloud-generator/blob/main/Word%20generation%20image.webp

## Features
- **Text Input**: Paste your text and generate a word cloud based on the most frequently used words.
- **Customizable Options**: Choose between a rectangle or circular word cloud, select from various color palettes, and choose a white or black background.
- **Stopwords Exclusion**: Exclude specific words from appearing in the word cloud by providing a comma-separated list.
- **User-Friendly Interface**: Interactive and easy-to-use with a Gradio frontend.

## Requirements

- Python 3.6 or higher
- `gradio`
- `nltk`
- `wordcloud`
- `matplotlib`
- `PIL` (Pillow)

You can install the necessary libraries using `pip`:

pip install gradio nltk wordcloud matplotlib Pillow
