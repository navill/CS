from db import db_manager
from utils import get_html
import cgi

def post_list(environ, start_response):
    query_set = db_manager.get_queryset()

    posts = []
    for query in query_set:
        posts.append({'id' : query[0], 'title' : query[1]})

    context = {'posts' : posts}

    start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])

    response= get_html('post_list.html', context).split('\n')
    return (line.encode() for line in response)

def post_detail(environ, start_response):
    id_arg = environ.get('args', '').rstrip('/')

    post = db_manager.retrieve_post(id_arg)

    id = post[0]
    title = post[1]
    content = post[2]

    context = {'id' : id, 'title' : title, 'content' : content}

    start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])

    response= get_html('post_detail.html', context).split('\n')
    return (line.encode() for line in response)

def post_create(environ, start_response):
    if environ['REQUEST_METHOD']=='POST':
        form = cgi.FieldStorage(environ['wsgi.input'], environ=environ)
        title = form.getvalue('title')
        content = form.getvalue('content')

        db_manager.create_post(title, content)
        start_response('303 SeeOther', [('Content-Type','text/html;charset=utf-8'), ('Location', 'http://localhost:8000/')])
        response= ['post_create']
        return (line.encode() for line in response)
    else:
        start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])
        response= get_html('post_form.html').split('\n')
        return (line.encode() for line in response)

def post_update(environ, start_response):
    id_arg=environ.get('args', '').split('/')[0]
    if environ['REQUEST_METHOD']=='POST':
        form=cgi.FieldStorage(environ['wsgi.input'], environ=environ)
        new_title=form.getvalue('title')
        new_content=form.getvalue('content')

        db_manager.update_post(id_arg, new_title, new_content)

        start_response('303 SeeOther', [('Content-Type','text/html;charset=utf-8'), ('Location', 'http://localhost:8000/')])
        response=['post_update']
        return (line.encode() for line in response)
    else:
        post=db_manager.retrieve_post(id_arg)
        old_title=post[1]
        old_content=post[2]

        start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        response=get_html('post_form.html', {'title' : old_title, 'content' : old_content}).split('\n')
        return (line.encode() for line in response)

def post_delete(environ, start_response):
    if environ['REQUEST_METHOD'] == 'POST':
        id_arg = environ.get('args', '').split('/')[0]
        db_manager.delete_post(id_arg)
        start_response('303 SeeOther', [('Content-Type','text/html;charset=utf-8'), ('Location', 'http://localhost:8000/')])
        response= ['post_delete']
        return (line.encode() for line in response)
    else:
        start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])
        response= get_html('post_confirm_delete.html').split('\n')
        return (line.encode() for line in response)
