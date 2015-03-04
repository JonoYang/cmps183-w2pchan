# -*- coding: utf-8 -*-
from datetime import datetime
from gluon import *

def get_ip():
    return current.request.client

db.define_table('board', 
                Field('name'))

db.define_table('thread',
                Field('board_id', db.board, readable = False, 
                        writable = False),
                Field('title'),
                Field('author'),
                Field('author_id', db.auth_user, readable = False, 
                        writable = False, default = auth.user_id),
                Field('author_ip', default = get_ip()),
                Field('date_created', 'datetime', readable = False,
                        writable = False, default = datetime.utcnow()),                
                Field('body', 'text'),
                Field('image', 'upload'))

db.define_table('post',
                Field('thread_id', db.thread, readable = False, 
                        writable = False),
                Field('author'),
                Field('author_id', db.auth_user, readable = False, 
                        writable = False, default = auth.user_id),
                Field('author_ip', default = get_ip()),
                Field('date_created', 'datetime', readable = False,
                        writable = False, default = datetime.utcnow()),
                Field('body', 'text'),
                Field('image', 'upload'))