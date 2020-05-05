import matplotlib.pyplot as plt
import os

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

# TODO: Move to place where this function belongs
    # def check_dicts
def calculate_emotions():
    df = speeches.load()
    df = speeches.clean(df)
    df['emotions'] = df.apply(lambda row:
                            calculator.get_emotions(row['speech']), axis = 1)
    df['total words'] = df.apply(lambda row:
                        calculator.count_words(row['speech']), axis = 1)
    for emotion in EMOTION_LIST:
        df[emotion] = df.apply(lambda row:
                row['emotions'][emotion] / row['total words'], axis = 1)
    return df