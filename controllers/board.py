def index():
    board_id = request.args(0)
    board_name = db.board[board_id].name
    threads = db(db.thread.board_id == board_id).select(orderby =~ db.thread.date_created)

    form = SQLFORM.factory(Field('title'),
                        Field('author'),
                        Field('image', 'upload', uploadfolder = 'applications/w2pchan/uploads'),
                        Field('body', 'text'),
                        table_name = 'thread')
    if form.process().accepted:
        board_id = request.args(0)
        db.thread.insert(author = form.vars.author, board_id = board_id,
                            title = form.vars.title, image = form.vars.image,
                            body = form.vars.body)
        shit =  db(db.thread).select().last().id
        redirect(URL('thread', 'index', args=[shit]))
    return dict(threads = threads, board_id = board_id, board_name = board_name, form = form)
