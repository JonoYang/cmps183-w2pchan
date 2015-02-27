def index():
    threads = db(db.thread.board_id == request.args(0)).select(orderby =~ db.thread.date_created)
    return dict(threads = threads)
