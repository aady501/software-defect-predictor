# This is a sample Python script.
import sys

from localrepository import LocalRepository


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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
