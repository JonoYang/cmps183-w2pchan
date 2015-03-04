def new():
    thread_id = request.args(0)
    form = SQLFORM(db.post)
    if form.process().accepted:
        db.post.insert(thread_id = thread_id, author = form.vars.author, 
                        body = form.vars.body, image = form.vars.image)
        redirect(URL('thread', 'index', args = [thread_id]))
    return dict(form = form)

@auth.requires_login()
def delete():
    post = db.post(request.args(0))
    if post.author_id != auth.user_id:
    	redirect(URL(''))