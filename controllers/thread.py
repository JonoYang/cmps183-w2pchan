# Steven Esser (sesser@ucsc.edu) 
# Jonathan Yang (jyang37@ucsc.edu)
#
# thread.py -- thread controller for w2pchan threads

from datetime import datetime

def index():
    
    # get the posts associated in a particular thread (thread id)
    thread_id = request.args(0)
    posts = db(db.post.thread_id == thread_id).select(orderby = db.post.date_created)
    thread = db.thread[request.args(0)]
    board_name = db.board[thread.board_id].name

    # form for the creation of posts. post creation handled in the post.py controller
    form = SQLFORM.factory(Field('author'),
                           Field('image', 'upload', uploadfolder = 'applications/w2pchan/uploads'),
                           Field('body', 'text'),
                           table_name = 'post')
    if form.process().accepted:
        if auth.user:
            db.post.insert(thread_id = thread_id, 
                           author = form.vars.author, 
                           body = form.vars.body, 
                           image = form.vars.image)
            db.thread[thread_id].update_record(date_updated = datetime.utcnow())
            redirect(URL('thread', 'index', args = [thread_id]))
        else:
            response.flash = 'Not logged in'

    return dict(posts = posts, 
                thread = thread, 
                form = form, 
                board_name = board_name)

@auth.requires_login()
def delete():

    # get the thread to delete
    thread = db.thread(request.args(0))
    board_id = thread.board_id
    confirm = ''

    # handle thread deletion
    # users can only delete their own threads
    if thread.author_id != auth.user_id:
        session.flash = 'Not authorized'
        redirect(URL('board', 'index', args = [board_id]))
    else:
        confirm = FORM.confirm('Are you sure you want to delete this thread?')
        if confirm.accepted:
            db(db.thread.id == thread.id).delete()
            redirect(URL('board', 'index', args = [board_id]))

    return dict(confirm = confirm)
