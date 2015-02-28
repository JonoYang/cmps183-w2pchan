def index():
    thread_id = request.args(0)
    posts = db(db.post.thread_id == thread_id).select(orderby =~ db.post.date_created)
    thread = db.thread[request.args(0)]

    form = SQLFORM.factory(Field('author'),
                            Field('image', 'upload', uploadfolder = 'applications/w2pchan/uploads'),
                            Field('body', 'text'),
                            table_name = 'post')
    if form.process().accepted:
        db.post.insert(thread_id = thread_id, author = form.vars.author, 
                        body = form.vars.body, image = form.vars.image)
        redirect(URL('thread', 'index', args = [thread_id]))
    return dict(posts = posts, thread = thread, form = form)

def new():
    form = SQLFORM(db.thread)
    if form.process().accepted:
        board_id = request.args(0)
        db.thread.insert(board_id = board_id, title = form.vars.title, body = form.vars.body)
        redirect(URL('thread', 'index', args=[form.vars.id]))
    return dict(form = form)
