from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import Response

import requests
import os
import json

BACKEND_URL = os.environ['BACKEND_URL']  # From docker-compose.yml
FRONTEND_PORT = 6543                     # This is the port number for the frontend server



#----------------------Helper Functions-------------------------
def show_home(req):
    return render_to_response('templates/home.html', {}, request=req)

def show_users(req):
    response = requests.get(BACKEND_URL + "/get_users")
    if (response.status_code == 200):
        users = response.json()
        return render_to_response('templates/users.html', {"users": users}, request=req)
    else:
        return Response(response.text)

def show_tello(req):
    response = requests.get(BACKEND_URL + "/get_tello_moves")
    if (response.status_code == 200):
        history = response.json()
        return render_to_response('templates/show_tello_moves.html', {"history": history}, request=req)
    else:
        return Response(response.text)


def add_user(req):
    new_user = req.POST.mixed()
    response = requests.post(BACKEND_URL + "/add_user", data=new_user)
    # If POST accepted
    if (response.status_code == 201):
        # Decide what to do with a after adding user!
        return show_users(req)
    else:
        return Response("Error: Please check your form for correct field names. They MUST match the keys of the DB dictionary!")

def add_user_page(req):
    response = requests.get(BACKEND_URL + "/get_users")
    if (response.status_code == 200):
        users = response.json()
        new_num=str(len(users))
        return render_to_response("templates/add_user_page.html",{"new_num":new_num},request=req)
    else:
        return Response("something weird happened")



def edit_user(req):#=========================================================
    print("\n\n\nin edit user front\n\n\n")
    new_user = req.GET.mixed()
    response = requests.post(BACKEND_URL + "/edit_user", data=new_user)
    return show_users(req)


def edit_user_page(req):
    page_data = req.GET.mixed()
    row_num=int(page_data['row_number'])

    response = requests.get(BACKEND_URL + "/get_users")
    users = response.json()
    print(users[row_num])
    if row_num <= len(users):
        if (response.status_code == 200):
            a_user=users[row_num]
            a_user["row"]=str(row_num)
            return render_to_response('templates/edit_user_page.html', {"user": a_user}, request=req)
        else:
            return Response(response.text)
    else:
        return Response("invalid row number")
 
def get_log(req):
    print("\n\n\nbefore backend")
    the_request=requests.get(BACKEND_URL + '/fake_data')
    print('\n')
    print(the_request.json())
    print("\n")
    return Response(json.dumps(the_request.json()))

if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')


    #--------------------------Routes---------------------------
    # Route for default route
    config.add_route('foo', '/')
    config.add_view(show_home, route_name='foo')

    # Route to view users
    config.add_route('show_users', '/show_users')
    config.add_view(show_users, route_name='show_users')

    # Route to add a user
    # NOTE: request_method='POST'
    
    config.add_route('add_user', '/add_user')
    config.add_view(add_user, route_name='add_user', request_method='POST')
    config.add_route('add_user_page', '/add_user_page')
    config.add_view(add_user_page, route_name='add_user_page')

    #CB routes ---------------------------
    # Route to edit a user
    # Add route to edit user (PUT request)
    config.add_route('edit_user', '/edit_user')
    config.add_view(edit_user, route_name='edit_user', request_method='GET')
    config.add_route('rt_edit_user_page', '/edit_user_page')
    config.add_view(edit_user_page, route_name='rt_edit_user_page')

    # Route to show moves

    # Add route to show moves (GET request)
    # NOTE: Use 'show_users' as inspiration
    # NOTE: route must be '/show_moves'
    config.add_route('rt_show_tello', '/show_tello_moves')
    config.add_view(show_tello, route_name='rt_show_tello', request_method='GET')

    config.add_route('rt_getdat','/fake_data')
    config.add_view(get_log, route_name='rt_getdat',request_method='GET')

    #------------------------Add static view (for css)----------
    config.add_static_view(name='/', path='./public', cache_max_age=3600)


    # Create 'app' and server and run it forever!
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', FRONTEND_PORT, app)
    print("\n\nfront end link locations\nhttp://localhost:6543\n\n\n")
    server.serve_forever()