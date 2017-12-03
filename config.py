# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

db_name = basedir.split('/')[-1] + '.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, db_name)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SECRET_KEY = 'tsftw'
SQLALCHEMY_TRACK_MODIFICATIONS = False

oauth_access_token = 'EAAIILRbWsnMBADR3bdTDzoVRGxNEieHvu9fGZCkRW3YG9731poCvRxptoBQ2ZBoCZC2XsL9nTe58xPxSkkcZBjK6WDUZBQZBBTxpumoBRa2vynoDsQSI5RGrr725uKJhYV8aaFTpQlNWeY9B5Yv8IiYqMgb7M3MByadcc2lJxs1AZDZD'
