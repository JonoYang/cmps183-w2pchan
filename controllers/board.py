from datetime import datetime

def index():
    if request.vars['page'] == None:
      page = 0
    if request.vars['page'] != None:
      # we are on a page, so determine which threads to show
      # ALSO, we are assuming page 1 is actually the next paginated page
      page = int(request.vars['page'])
      min = page * 10 # set the next subset of threads 
      max = min + 10
    else:
      min=0
      max=10

    # define the tuple limit by for db query
    limitby=(min,max)

    board_id = request.args(0)
    board_name = db.board[board_id].name
    threads = db(db.thread.board_id == board_id).select(orderby =~ db.thread.date_updated, limitby=limitby)
    rec_post = {}
    for t in threads:
        posts = db(db.post.thread_id == t.id).select(orderby = db.post.date_created)
        rec_post[t.id] = posts[:3]

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
                db.thread.insert(author = form.vars.author, board_id = board_id,
                                title = form.vars.title, date_updated = datetime.utcnow(),
                                image = form.vars.image,
                                body = form.vars.body)
                shit =  db(db.thread).select().last().id
                redirect(URL('thread', 'index', args=[shit]))               
        else:
            response.flash = 'Not logged in'
    return dict(threads = threads, board_id = board_id, board_name = board_name, form = form, rec_post = rec_post, page = page)
