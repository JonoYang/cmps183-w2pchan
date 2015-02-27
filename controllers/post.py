
def new():
    thread_id = request.args(0)
    form = SQLFORM(db.post)
    if form.process().accepted:
        db.post.insert(thread_id = thread_id, author = form.vars.author, 
                        body = form.vars.body, image = form.vars.image)
        redirect(URL('thread', 'index', args = [thread_id]))
    return dict(form = form)