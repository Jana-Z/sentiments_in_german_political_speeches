import matplotlib.pyplot as plt
import os
import pandas as pd

import speeches
import emotions
from emotions import data 
from emotions import stemmer
from emotions import calculator

COLOR_DICT = {
    'ekel': 'g', 
    'freude': 'y',
    'furcht': 'm',
    'liebe': 'lightpink',
    'trauer': 'b',
    'überraschung': 'gold',
    'verachtung': 'gray',
    'wut': 'r'
}

EMOTIONS_TRANSLATION = {
    'ekel': 'disgust', 
    'freude': 'joy',
    'furcht': 'fright',
    'liebe': 'love',
    'trauer': 'grief',
    'überraschung': 'surprise',
    'verachtung': 'contempt',
    'wut': 'anger'
}     

def plot_per_year_all_emotions(df, emotion_list, dst=None):
    fig, ax = plt.subplots()
    for emotion in emotion_list:
        color = COLOR_DICT[emotion] if emotion in COLOR_DICT else 'b'
        ax = df.plot(
            x ='date',
            y=emotion,
            kind = 'scatter',
            color=color,
            ax=ax
        )
    ax.legend(emotion_list)
    if dst:
        filepath = os.path.join(dst, emotion + '_scatter.png')
        print(f'saving file to: {filepath}')
        plt.savefig(filepath)
    else:
        plt.show()
    plt.clf()    

def plot_per_year(df, emotion, dst=None):
    color = COLOR_DICT[emotion] if emotion in COLOR_DICT else 'b'
    df.plot(
        x ='date',
        y=emotion,
        kind = 'scatter',
        color=color,
        title=emotion                                                    \
            + '(' + EMOTIONS_TRANSLATION[emotion] + ') per year'     \
            if emotion in EMOTIONS_TRANSLATION else 'per year' 
        )
    if dst:
        filepath = os.path.join(dst, emotion + '_scatter.png')
        print(f'saving file to: {filepath}')
        plt.savefig(filepath)
    else:
        plt.show()
    plt.clf()

def plot_average_score(df, emotion_list, dst=None):
    df.plot.box(figsize=(8,6), y=emotion_list)
    if dst:
        plt.savefig(os.path.join(dst, 'box_plot'))
    else:
        plt.show()
    plt.clf()

def plot_mean_per_year(df, emotion, dst=None):
    color = COLOR_DICT[emotion] if emotion in COLOR_DICT else 'b'
    df.groupby(['date']).mean()[emotion].plot(color=color,
        title='mean of ' + emotion                                  \
            + '(' + EMOTIONS_TRANSLATION[emotion] + ') per year'   \
            if emotion in EMOTIONS_TRANSLATION else 'per year'     \
        )
    if dst:
        filepath = os.path.join(dst, emotion + '_line.png')
        print(f'saving file to: {filepath}')
        plt.savefig(filepath)
    else:
        plt.show()
    plt.clf()

def plot_mean_per_year_all_emotions(df, emotion_list, dst=None):
    fig, ax = plt.subplots()
    for emotion in emotion_list:
        color = COLOR_DICT[emotion] if emotion in COLOR_DICT else 'b'
        ax = df.groupby(['date']).mean()[emotion].plot(
            x='date',
            y=emotion,
            kind='line',
            color=color,
            ax=ax
        )
    ax.legend(emotion_list)
    if dst:
        filepath = os.path.join(dst, emotion + '_scatter.png')
        print(f'saving file to: {filepath}')
        plt.savefig(filepath)
    else:
        plt.show()
    plt.clf()

def plot_pie_per_politicians(df, emotion_list, politician, dst=None, n=6):
    # only plot n most occuring politicians in data set
    politicians = df['speaker'].value_counts()[:n].index.tolist()
    politician_df = pd.DataFrame({})
    for emotion in emotion_list:
        for politician in politicians:
            politician_df.at[emotion, politician] = (df.loc[df['speaker'] == politician][emotion]).mean()
    politician_df *= 1000   # scale for pie plot
    print(politician_df)
    politician_df.plot.pie(subplots=True, figsize=(3,3), layout=(2, 3), legend=False)
    plt.show()
