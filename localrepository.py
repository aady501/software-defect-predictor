"""
file: localrepository.py
author: Ben Grawi <bjg1568@rit.edu>
date: October 2013
description: Holds the repository abstraction class
"""
import shutil
# from ingester.git import *
# from orm.commit import *

from datetime import datetime
import os
import logging

import pandas as pd

from git import Git


class Repo():

    def __init__(self, url, id):
        self.id = id
        self.url = url


class LocalRepository():
    """
    Repository():
    description: Abstracts the actions done on a repository
    """
    repo = None
    adapter = None
    start_date = None

    def __init__(self, repo_url):
        """
        __init__(path): String -> NoneType
        description: Abstracts the actions done on a repository
        """

        # Temporary until other Repo types are added
        self.adapter = Git

        self.commits = {}

        self.repo = Repo(repo_url, '1')

    def sync(self):
        """
        sync():
        description: Simply wraps the syncing functions together
        """

        # TODO: Error checking.
        firstSync = self.syncRepoFiles()
        # self.syncCommits(firstSync)
        # self.printCommits(firstSync)
        self.createdf()
        # Set the date AFTER it has been ingested and synced.
        # self.repo.ingestion_date = self.start_date

    def syncRepoFiles(self):
        """
        syncRepoFiles() -> Boolean
        description: Downloads the current repo locally, and sets the path and
            injestion date accordingly
        returns: Boolean - if this is the first sync
        """
        # Cache the start date to set later
        self.start_date = str(datetime.now().replace(microsecond=0))

        path = os.path.dirname(__file__) + self.adapter.REPO_DIRECTORY + self.repo.id
        # See if repo has already been downloaded, if it is pull, if not clone
        if os.path.isdir(path):
            shutil.rmtree(path)
        os.makedirs(path, )
        self.adapter.clone(self.adapter, self.repo)
        firstSync = True

        return firstSync

    def printCommits(self, firstSync):
        """
        syncCommits():
        description: Makes each commit dictonary into an object and then
            inserts them into the database
        arguments: firstSync Boolean: whether to sync all commits or after the
            ingestion date
        """
        commits = self.adapter.log(self.adapter, self.repo)
        # commitsSession = Session()
        # logging.info('Saving commits to the database...')
        for commitDict in commits:
            print(commitDict)
        # commitsSession.commit()
        # commitsSession.close()
        # logging.info('Done saving commits to the database.')

    def createdf(self):
        commits = self.adapter.log(self.adapter, self.repo)
        df = pd.DataFrame(commits)
        return df
