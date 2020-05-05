import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_per_speaker(df):
    speakers = df.speaker.unique()
    y_pos = np.arange(len(speakers))
    number_of_speeches = df['speaker'].value_counts().values

    plt.barh(y_pos, number_of_speeches, align='center', alpha=1)
    plt.yticks(y_pos, speakers)
    plt.xlabel('no of speeches')
    plt.title('Speeches per speaker in dataset')

    plt.show()

def print_per_year(df):
    print(df.set_index(['speech', 'date']).count(level='date'))

def plot_per_year(df, dst=None):
    df.groupby('date').count()['speech'].plot(kind='bar', title='Number of speeches per year in dataset')
    if dst:
        plt.savefig(os.path.join(dst, 'quantities_per_year.png'))
    else:
        plt.show()
    plt.clf()