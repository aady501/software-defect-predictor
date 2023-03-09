# This is a sample Python script.
import os
import sys

from localrepository import LocalRepository
from model import predict
import pandas as pd

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ''
    local_repo = LocalRepository(arg)
    local_repo.sync()
    df_test = local_repo.createdf()
    df_predicted = predict(df_test)
    df_predicted.to_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'predicted.csv'), index=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
