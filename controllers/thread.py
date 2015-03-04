def index():
    thread_id = request.args(0)
    posts = db(db.post.thread_id == thread_id).select(orderby =~ db.post.date_created)
    thread = db.thread[request.args(0)]

    form = SQLFORM.factory(Field('author'),
                            Field('image', 'upload', uploadfolder = 'applications/w2pchan/uploads'),
                            Field('body', 'text'),
                            table_name = 'post')
    if form.process().accepted:
        if auth.user:
            db.post.insert(thread_id = thread_id, author = form.vars.author, 
                        body = form.vars.body, image = form.vars.image)
            redirect(URL('thread', 'index', args = [thread_id]))
        else:
            response.flash = 'Not logged in'
    return dict(posts = posts, thread = thread, form = form)
