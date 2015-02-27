# -*- coding: utf-8 -*-
from datetime import datetime
from gluon import *

def ip():
    return current.request.client

db.define_table('post',
                Field('author'),
                Field('author_ip', writable = False, readable = False, 
                        default = ip()),
                Field('date_created', 'datetime', writable = False,
                        default = datetime.utcnow()),
                Field('image', 'upload'),
                Field('body', 'text')
                )

db.define_table('thread',
                Field('author'),
                Field('author_ip', writable = False, readable = False,
                        default = ip()),
                Field('date_created', 'datetime', writable = False,
                        default = datetime.utcnow()),
                Field('posts', db.post)
                )