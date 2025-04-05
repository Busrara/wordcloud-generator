# -*- coding: utf-8 -*-

import numpy as np
import nltk
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
from PIL import Image, ImageDraw
import os
import matplotlib
matplotlib.use('Agg')  # Set Matplotlib backend to Agg
import matplotlib.pyplot as plt
import io

class WordCloudGenerator:
    """A simple and reliable word cloud generator with customization options"""

    def __init__(self):
        self._setup_nltk()
        self.stopwords = set(nltk.corpus.stopwords.words('english'))
        self.stopwords.update(STOPWORDS)

    def _setup_nltk(self):
        """Set up NLTK data directory and download required data"""
        nltk_data_dir = os.path.expanduser("~/nltk_data")
        os.makedirs(nltk_data_dir, exist_ok=True)
        nltk.download('punkt', download_dir=nltk_data_dir, quiet=False)
        nltk.download('stopwords', download_dir=nltk_data_dir, quiet=False)
        nltk.data.path.append(nltk_data_dir)

    def _create_circular_mask(self, height=500, width=1000):
        y, x = np.ogrid[:height, :width]
        center = (height/2, width/2)
        radius = min(center[0], center[1]) * 0.9
        mask = ((x - center[1])**2 + (y - center[0])**2) <= radius**2
        return 255 * mask.astype(int)

    def generate(self, text, shape="rectangle", palette="viridis", bg_color="white"):
        if not text or len(text) < 50:
            return self._create_error_image("More text required (minimum 50 characters)")

        tokens = nltk.word_tokenize(text)
        tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in self.stopwords and len(word) > 1]

        if len(tokens) < 10:
            return self._create_error_image("More meaningful words required (minimum 10)")

        mask = None
        if shape == "circle":
            mask = self._create_circular_mask()

        wc = WordCloud(
            width=800,
            height=400,
            background_color=bg_color,
            max_words=100,
            colormap=palette,
            stopwords=self.stopwords,
            mask=mask,
            contour_width=1 if mask is not None else 0,
            contour_color='steelblue' if mask is not None else None,
            prefer_horizontal=0.9
        )

        word_freq = Counter(tokens)
        wc.generate_from_frequencies(word_freq)

        return self._wordcloud_to_image(wc)

    def _wordcloud_to_image(self, wordcloud):
        try:
            return Image.fromarray(wordcloud.to_array())
        except Exception as e:
            try:
                plt.figure(figsize=(8, 4), dpi=100)
                plt.imshow(wordcloud, interpolation="bilinear")
                plt.axis("off")
                plt.tight_layout(pad=0)
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                img = Image.open(buf)
                plt.close()
                return img
            except Exception as e2:
                return self._create_error_image("Failed to create image")

    def _create_error_image(self, message):
        img = Image.new('RGB', (800, 400), color='#f0f0f0')
        draw = ImageDraw.Draw(img)
        draw.text((50, 180), f"ERROR: {message}", fill="red")
        return img

    def add_stopwords(self, text):
        if text:
            words = [word.strip() for word in text.split(',')]
            self.stopwords.update([w.lower() for w in words if w])
