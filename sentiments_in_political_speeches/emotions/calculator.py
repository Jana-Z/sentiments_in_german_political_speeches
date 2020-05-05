import re

from . import data
from . import stemmer

def _split_sentences(text):
    text = text.strip()
    sentences = re.split(r'[.?!]+', text)
    sentences = [s.strip() for s in sentences]
    return sentences[:-1]

def _split_words(text):
    words = re.findall(r'\w+', text)
    words = [w.strip() for w in words]
    return words

def count_words(text):
    words = re.findall(r'\w+', text)
    return len(words) if len(words) != 0 else 1   # not to divide by zero in main.py

def get_emotions(speech):
    emotions_dict, stopwords = data.emotions_loader.load_all()
    emotions_in_speech = {}
    emotion_list = data.emotions_loader.get_emotion_list()
    sentences = _split_sentences(speech)
    for sentence in sentences:
        words = _split_words(sentence)
        for word in words:
            word = stemmer.stem(word)
            if word not in stopwords:
                if word in emotions_dict:
                    emotion = emotions_dict[word]
                    if emotion in emotions_in_speech:
                        emotions_in_speech[emotion].append(word)
                    else:
                        emotions_in_speech[emotion] = [word]
    return_dict = {k: len(v) for k, v in emotions_in_speech.items()}
    if len(return_dict.keys()) != len(emotion_list):
        for emotion in emotion_list:
            if emotion not in  return_dict:
                return_dict[emotion] = 0
    return return_dict
        


def get_emotions_per_sentence(text):
    emotions_dict, stopwords = data.emotions_loader.load_all()
    emotions_in_speech = {}