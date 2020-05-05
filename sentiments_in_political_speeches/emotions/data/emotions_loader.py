import csv
import os

EMOTION_LIST = ['ekel', 'freude', 'furcht', 'liebe', 'trauer', 'überraschung', 'verachtung', 'wut']
EMOTION_DIR = './emotions/data/emotionsstemmed/'        # invoked from main.py
STOP_WORDS_PATH = './emotions/data/stopwords.txt'

def load_all(inverted = True):
    emotion_dict = dict()
    for emotion in EMOTION_LIST:
        emotion_dict[emotion] = load_csv_file(
            os.path.join(EMOTION_DIR, emotion + '.txt')
        )
    if inverted:
        emotion_dict = {k : v.keys() for k, v in emotion_dict.items()}
        emotion_dict = {v1: k for k, v in emotion_dict.items() for v1 in v}
    stop_words = return_file_by_line(STOP_WORDS_PATH)
    return emotion_dict, stop_words

def load_csv_file(filepath, threshold=None):
    # comma seperated
    if os.path.isfile(filepath):
        with open(filepath, 'r', newline = '') as f:                                                                                          
            reader = csv.reader(f, delimiter=',')
            if not threshold:
                return dict([key, float(value)]
                    for key, value in dict(reader).items())
            else:
                return dict([key, float(value)]
                    for key, value in dict(reader).items()  
                    if float(value) > threshold)
    else:
        raise OSError('filepath to emotions_dict is not a path to a file')

def return_file_by_line(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            content = f.readlines()
        return [c.strip() for c in content]
    else:
        raise OSError('filepath to stopwords is not a path to a file')

def get_emotion_list():
    return EMOTION_LIST