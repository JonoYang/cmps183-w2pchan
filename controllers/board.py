def index():
    board = db.board[request.args(0)]
    threads = db(db.thread.board_id == board.id).select(orderby =~ db.thread.date_created)
    return dict(threads = threads, board = board)
