"""
__author__ = "Shrikanth N.C. (https://snaraya7.github.io/)"
"""
import os

from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']


def normalize(df: pd.DataFrame):
    """
  Log Normalization
  """
    for c in [c for c in df.columns if df[c].dtype in numerics]:
        if c != 'contains_bug' and c != 'fix' and c != 'loc' and c != 'author_email':
            df[c] = df[c] + 0.0000001
            df[c] = np.log10(df[c])
    return df


def toNominal(changes):
    releaseDF = changes
    releaseDF.loc[releaseDF['contains_bug'] >= 1, 'contains_bug'] = 1
    releaseDF.loc[releaseDF['contains_bug'] <= 0, 'contains_bug'] = 0
    d = {1: True, 0: False}
    releaseDF['contains_bug'] = releaseDF['contains_bug'].map(d)
    return releaseDF


def pre_process_train(df: pd.DataFrame):
    df_new = df.fillna(0)
    df_new = normalize(df_new)
    df_new = toNominal(df_new)
    df_new = df_new[(df_new['contains_bug'] == True) | (df_new['contains_bug'] == False)]
    return df_new


def pre_process_test(df: pd.DataFrame):
    df_new = df.fillna(0)
    df_new['la'] = pd.to_numeric(df_new['la'])
    df_new['lt'] = pd.to_numeric(df_new['lt'])
    df_new = normalize(df_new)
    # TODO: handle negative lt values being turned to NaN
    df_new = df_new[~df_new['lt'].isna()]
    return df_new

def early_sample(training_dataframe, default=25):
    # sort training data by time asc
    training_dataframe = training_dataframe.head(150).copy(deep=True)
    buggyChangesDF = training_dataframe[training_dataframe['contains_bug'] == True]
    nonBuggyChangesDF = training_dataframe[training_dataframe['contains_bug'] == False]
    sample_size = min(default, min(len(buggyChangesDF), len(nonBuggyChangesDF)))

    return buggyChangesDF.sample(sample_size).copy(deep=True).append(
        nonBuggyChangesDF.sample(sample_size).copy(deep=True)).copy(deep=True)


def predict(test_dataframe):
    """
  Return predictions to the caller
  """
    training_data = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'training_data.csv'))
    training_data = pre_process_train(training_data)
    test_dataframe = pre_process_test(test_dataframe)
    training_data = early_sample(training_data)

    temp = training_data[['la', 'lt', 'contains_bug']]
    trainY = temp.contains_bug
    trainX = temp.drop(labels=['contains_bug'], axis=1)
    classifier = LogisticRegression()
    classifier.fit(trainX, trainY)

    test_dataframe = test_dataframe.copy(deep=True)
    predictions = classifier.predict(test_dataframe[['la', 'lt']])
    test_dataframe['contains_bug'] = predictions

    return test_dataframe
