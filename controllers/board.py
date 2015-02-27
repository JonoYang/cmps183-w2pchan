def index():
    board_id = request.args(0)
    board_name = db.board[board_id].name
    threads = db(db.thread.board_id == board_id).select(orderby =~ db.thread.date_created)

    form = SQLFORM(db.thread)
    if form.process().accepted:
        board_id = request.args(0)
        db.thread.insert(board_id = board_id, title = form.vars.title, body = form.vars.body)
        redirect(URL('thread', 'index', args=[form.vars.id]))
    return dict(threads = threads, board_id = board_id, board_name = board_name, form = form)
