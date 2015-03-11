# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

def index():
    boards = db().select(orderby = db.board.id) 
    pics = ["http://financeandcareer.com/wp-content/uploads/2013/03/webProgrammingInternship.jpg",
            "http://www.freemake.com/blog/wp-content/uploads/2014/09/streaming-music.jpg",
            "http://thumb7.shutterstock.com/display_pic_with_logo/700705/135069491/stock-vector-fitness-and-healthy-exercise-word-and-icon-cloud-135069491.jpg",
            "http://images.anbmedia.com/articles/videogamereviews/icon.png",
            "http://1.bp.blogspot.com/-qJA7dW3W-M0/VH4l2LQUIEI/AAAAAAAAACo/ZJqeqHgpmBs/s1600/books.png",
            "http://www.shockmansion.com/wp-content/myimages/2013/05/Posted-On-Shock-Mansion1.jpg"]

    return dict(boards = boards, pics = pics)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
