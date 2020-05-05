import os 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import collections
from itertools import cycle, islice

from readability import plotter as read
import speeches

from emotions import data 
from emotions import stemmer
from emotions import calculator

from plotting import emotions_plotter
from plotting import quantities_plotter

# Dataset from: http://adrien.barbaresi.eu/corpora/speeches/#data

DST_DIR = './plotting/plots_big/'

def main():
    emotion_list = data.emotions_loader.get_emotion_list()
    df = pd.read_csv('speeches.csv')
    # quantities.plot_per_year(df)
    # emotions_plotter.plot_average_score(df,
    #     emotion_list=emotion_list,
    #     dst=os.path.join(DST_DIR, 'emotions/')
    # )
    # emotions_plotter.plot_per_year_all_emotions(
    #     df=df,
    #     emotion_list=emotion_list
    #     dst=os.path.join(DST_DIR, 'emotions/total')
    # )
    # emotions_plotter.plot_mean_per_year_all_emotions(
    #     df=df,
    #     emotion_list=emotion_list, 
    #     dst=os.path.join(DST_DIR, 'emotions/mean'))
    # for emotion in emotion_list:
    #     emotions_plotter.plot_mean_per_year(
    #         emotion=emotion,
    #         df=df,
    #         dst=os.path.join(DST_DIR, 'emotions/means')
    #     )
    #     emotions_plotter.plot_per_year(df=df,
    #         emotion=emotion,
    #         dst=os.path.join(DST_DIR, 'emotions/total')
    #     )
    emotions_plotter.plot_pie_per_politicians(df=df, emotion_list=emotion_list, politician=None)

def get_emotions_and_store(dst_filepath='./speeches.csv'):
    df = speeches.load()
    df = speeches.clean(df)
    df['emotions'] = df.apply(lambda row:
                            calculator.get_emotions(row['speech']), axis = 1)
    df['total words'] = df.apply(lambda row:
                        calculator.count_words(row['speech']), axis = 1)
    for emotion in EMOTION_LIST:
        df[emotion] = df.apply(lambda row:
                row['emotions'][emotion] / row['total words'], axis = 1)
    df.to_csv(dst_filepath)

if __name__ == '__main__':
    main()
