import os
import random

basedir = os.path.abspath(os.path.dirname(__file__))
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def generator(length):
    key = ''
    for i in range(length):
        key += random.choice(chars)
    return key

class Config(object):
    SECRET_KEY = generator(32)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
