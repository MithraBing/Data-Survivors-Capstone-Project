import re
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import rcParams
from nltk.corpus import stopwords
from IPython.display import display
import io

nltk.download('stopwords')

def save_fig(fig):
    filename = 'D:/Capstone/wordcloud.png' #local path to save the wordcloud image
    with open(filename, 'wb') as f:
        fig.savefig(f, format='png')

def generate_wordcloud(text):
    # Preprocessing the text: Remove stopwords, punctuation, spaces using NLP library
    stop_words = set(stopwords.words('english'))
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    words = text.split()
    cleaned_text = ' '.join(word for word in words if word not in stop_words)

    # Plotting the word cloud itself
    # Set the font to a TrueType font
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Arial']
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path='arial.ttf').generate(cleaned_text)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    #fetch current figure
    fig = plt.gcf()
    fig.set_size_inches(8, 6)
    save_fig(fig)

