# -*- coding: utf-8 -*-
from datetime import datetime
from gluon import *

def ip():
    return current.request.client

db.define_table('board', 
                Field('name'))

db.define_table('thread',
                Field('title'),
		Field('body', 'text'),
		Field('date_created', 'datetime', default = datetime.utcnow(), readable=False, writable=False),
		Field('board_id', db.board, readable=False, writable=False))

db.define_table('post',
                Field('author'),
                Field('date_created', 'datetime', readable = False, 
                        writable = False, default = datetime.utcnow()),
                Field('body', 'text'),
                Field('image', 'upload'),
		        Field('thread_id', db.thread, readable = False, writable = False))
