from datetime import datetime

def index():
    board_id = request.args(0)
    board_name = db.board[board_id].name
    threads = db(db.thread.board_id == board_id).select(orderby =~ db.thread.date_updated)
    posts = db(db.post).select()
    form = SQLFORM.factory(Field('title'),
                        Field('author'),
                        Field('image', 'upload', uploadfolder = 'applications/w2pchan/uploads'),
                        Field('body', 'text'),
                        table_name = 'thread')
    if form.process().accepted:
        if auth.user:
            if form.vars.image == '':
                response.flash = 'Image requred'
            else:
                board_id = request.args(0)
                db.thread.insert(author = form.vars.author, board_id = board_id,
                                title = form.vars.title, date_updated = datetime.utcnow(),
                                image = form.vars.image,
                                body = form.vars.body)
                shit =  db(db.thread).select().last().id
                redirect(URL('thread', 'index', args=[shit]))               
        else:
            response.flash = 'Not logged in'
    return dict(threads = threads, board_id = board_id, board_name = board_name, form = form, posts = posts)
