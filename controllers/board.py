def index():
    board_id = request.args(0)
    threads = db(db.thread.board_id == board_id).select(orderby =~ db.thread.date_created)
    return dict(threads = threads, board_id = board_id)
