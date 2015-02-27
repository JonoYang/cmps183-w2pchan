def index():
    posts = db(db.post.thread_id == request.args(0)).select(orderby =~ db.post.date_created)
    thread = db.thread[request.args(0)]
    return dict(posts = posts, thread = thread)

def new():
    form = SQLFORM(db.thread)
    if form.process().accepted:
        board_id = request.args(0)
        db.thread.insert(board_id = board_id, title = form.vars.title, body = form.vars.body)
        redirect(URL('thread', 'index', args=[form.vars.id]))
    return dict(form = form)
