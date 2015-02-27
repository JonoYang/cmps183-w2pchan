def index():
    posts = db(db.post.thread_id == request.args(0)).select(orderby =~ db.post.date_createod)
    return dict(posts = posts)
