"""
__author__ = "Shrikanth N.C. (https://snaraya7.github.io/)"
"""
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

def normalize(dataframe):
  """
  Log Normalization
  """
  for c in [c for c in dataframe.columns if dataframe[c].dtype in numerics]:
    if c != 'Buggy' and c != 'fix' and c != 'loc' and c != 'author_email':
      dataframe[c] = np.log10(dataframe[c])

  return dataframe

def early_sample(training_dataframe, default=25):

    buggyChangesDF = training_dataframe[training_dataframe['Buggy'] == True]
    nonBuggyChangesDF = training_dataframe[training_dataframe['Buggy'] == False]
    sample_size = min(default, min(len(buggyChangesDF), len(nonBuggyChangesDF)))

    return buggyChangesDF.sample(sample_size).copy(deep=True).append(
      nonBuggyChangesDF.sample(sample_size).copy(deep=True)).copy(deep=True)

def predict(test_dataframe):
  """
  Return predictions to the caller
  """

  training_data = normalize(pd.read_csv('training_data.csv'))
  training_data = early_sample(training_data)

  temp = training_data[ ['la', 'lt', 'Buggy'] ]
  trainY = temp.Buggy
  trainX = temp.drop(labels=['Buggy'], axis=1)
  classifier = LogisticRegression()
  classifier.fit(trainX, trainY)

  test_dataframe = test_dataframe.copy(deep=True)
  predictions = classifier.predict(test_dataframe[ ['la', 'lt']])
  test_dataframe['Buggy'] = predictions

  return test_dataframe
