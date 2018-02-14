# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

db_name = basedir.split('/')[-1] + '.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, db_name)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SECRET_KEY = 'tsftw'
SQLALCHEMY_TRACK_MODIFICATIONS = False

oauth_access_token = 'EAAIILRbWsnMBALtZAzx5BYfaBAnI9yeRZBqF4MZBugN3jU8S2WZBpwwOh1jsMBTvnPtwDak1qO8FU2LxnAxNDv6kmbsIXEJdQQJpgGX8JKz7QjEwlwnLg88lGSlxpR5Ri1OX7sujlNK9m5QZCDLvqIJufSIokenZAz9rdJ3rX5yAZDZD'
