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
    thread_id = post.thread_id
    confirm = ''
    if post.author_id != auth.user_id:
        session.flash = 'Not authorized, BITCH'
        redirect(URL('thread', 'index', args = [thread_id]))
    else:
        confirm = FORM.confirm('DO YOU WANT TO DELETE THIS, BITCH')
        if confirm.accepted:
            db(db.post.id == post.id).delete()
            redirect(URL('thread', 'index', args = [thread_id]))
    return dict(confirm = confirm)