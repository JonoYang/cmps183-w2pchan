# Steven Esser (sesser@ucsc.edu) 
# Jonathan Yang (jyang37@ucsc.edu)
#
# board.py -- board controller for w2pchan boards

from datetime import datetime

def index():
    
    # request.vars are the varibles directly after the relative path.
    # for example: '/board/1?&page=1'  request.vars = page : 1
    if request.vars['page'] != None:
      # we are on a page, so determine which threads to show
      # ALSO, we are assuming page 1 is actually the next paginated page
      page = int(request.vars['page'])
      min = page * 5 # set the next subset of threads 
      max = min + 5
    else:
      page = 0
      min=0
      max=5
    
    # set the subset of threads 
    limitby=(min,max)
    
    # get the corect threads for the specific board and specific subset of threads 
    board_id = request.args(0)
    board_name = db.board[board_id].name
    threads = db(db.thread.board_id == board_id).select(orderby =~ db.thread.date_updated, limitby=limitby)

    # determine max number of pages
    num_threads = 0
    for row in db(db.thread.board_id == board_id).select():
        num_threads+=1 
    
    # get max number of pages by dividing by the number of threads per page
    max_pages = num_threads / 5

    rec_post = {}
    post_count = {}

    # displays the most recent three posts in a particular thread.
    for t in threads:
        posts = db(db.post.thread_id == t.id).select(orderby = db.post.date_created)
        post_count[t.id] = len(posts)
        if len(posts) <= 3:
            rec_post[t.id] = posts[:3]
        else:
            rec_post[t.id] = posts[-3:]

    ## this section is for the thread submission form. requires login 
    ## thread creation is handled in the thread.py controller.
    form = SQLFORM.factory(Field('title'),
                           Field('author'),
                           Field('image', 'upload', uploadfolder = 'applications/w2pchan/uploads'),
                           Field('body', 'text'),
                           table_name = 'thread')
    if form.process().accepted:
        if auth.user:
            if form.vars.image == '':
                response.flash = 'Image requred'
            else:
                board_id = request.args(0)
                db.thread.insert(author = form.vars.author, 
                                 board_id = board_id,
                                 title = form.vars.title, 
                                 date_updated = datetime.utcnow(),
                                 image = form.vars.image,
                                 body = form.vars.body)
                shit =  db(db.thread).select().last().id
                redirect(URL('thread', 'index', args=[shit]))               
        else:
            response.flash = 'Not logged in'

    return dict(threads = threads, 
                board_id = board_id, 
                board_name = board_name, 
                form = form, 
                rec_post = rec_post, 
                page = page, 
                max_pages = max_pages, 
                post_count = post_count)
