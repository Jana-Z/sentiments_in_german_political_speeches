import os
import xmltodict
import pandas as pd
import numpy as np
import re

DIR_PATH = './speeches/data/'   # invoked from main.py
DATA_FILES = ['AuswärtigesAmt.xml', 'Bundespräsidenten.xml', 'Bundesregierung.xml', 'Bundestagspräsidenten.xml']

def load():
    return import_speeches_local(DIR_PATH, DATA_FILES)

def import_speeches_local(dir_path, data_files):
    print('Importing speeches...')
    dictionary = {'speaker' :[], 'date': [], 'speech': []}
    for data_file in data_files:
        xml_path = dir_path + '/' +  data_file
        if os.path.isfile(xml_path):
            with open(xml_path, mode="rb") as file: 
                xml_document = xmltodict.parse(file) 
                nodes = (xml_document['collection']['text'])
            dictionary['speaker'].extend([t['@person'] for t in nodes])
            dictionary['date'].extend([t['@datum'] for t in nodes])
            dictionary['speech'].extend([t['rohtext'] for t in nodes])
        else:
            raise OSError('Import speeches local failed. No such file or directory.')
    print('Import completed')
    return pd.DataFrame(dictionary)

def clean(df):
    df = df[df['speaker'] != 'k.A.']
    df.date = [re.findall(r'[[1-3][0-9]{3}', date)[0] for date in df.date]   # get years out of weird data formats
    df.date = df['date'].str.extract('(\d+)', expand=False).astype(int)
    sLength = len(df['speech'])
    df.set_index([pd.Index(np.arange(sLength))])
    return df

def create_subset(df):
    return df.groupby('speaker') \
        .apply(lambda g: g.sample(0 if len(g) < 50 else 50)) \
        .reset_index(drop=True)