# Create your views here.
from django.shortcuts import render_to_response,HttpResponse,redirect
from jBlog import settings
from django.http import HttpResponseForbidden
from jBlog.jauth.token_store import token_master
import json
import time
from django.contrib.sessions.backends.db import SessionStore

def GetAuthString(base_url = "https://accounts.google.com/o/oauth2/auth"):
    args = ["scope="+"+".join(settings.GOOGLE_AUTH_SETTINGS['scopes'])]
    args.append("response_type=code")
    args.append("redirect_uri="+settings.GOOGLE_AUTH_SETTINGS['redirect_url'])
    args.append("client_id="+settings.GOOGLE_AUTH_SETTINGS['client_id'])
    args.append('user_agent=adventuresinpy')
    return base_url+"?"+"&".join(args)
def StoreToken(token_data,my_dict=None):
    if my_dict==None:my_dict = {}
    my_dict['access_token'] = token_data['access_token']#short lived token
    my_dict['id_token']     = token_data['id_token']#refresh token
    my_dict['token_type']   = token_data['token_type']#bearer
    my_dict['expires'] = time.time()+token_data['expires_in']#seconds till expiry (3600sec or 1hour from issuance
    return my_dict
def google_oauth(request,extra=""):
    try:request.session['last_url']=request.GET['next']
    except :
        return HttpResponseForbidden()
    return redirect(GetAuthString())
    #return redirect("https://accounts.google.com/o/oauth2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Foath_callback&user_agent=adventuresinpy&client_id=867409884723-66j3vvh7drng6s2un9g8f9u67tap7ut8.apps.googleusercontent.com&response_type=code")
def fb_oauth(request,extra=""):
    return HttpResponseForbidden()
    #request.session['last_url']="refferer"
    return redirect("https://accounts.google.com/o/oauth2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Foath_callback&user_agent=adventuresinpy&client_id=867409884723-66j3vvh7drng6s2un9g8f9u67tap7ut8.apps.googleusercontent.com&response_type=code")

def oauth_response(request,response_data=''):
    try:code = request.GET['code']
    except KeyError:return HttpResponseForbidden()
    tok = token_master.get_token(code)
    result = token_master.sendToken('https://accounts.google.com/o/oauth2/token',tok)
    token_data = StoreToken(json.loads(result))
    #s = SessionStore()
    user_data = token_master.UserData(token_data['access_token'])
    request.session['token']={'goog':token_data}
    request.session['udata'] = user_data
    #s.save()
    try:return  redirect(request.session.pop("last_url"))
    except:return HttpResponseForbidden()
def login_or_profile(request,extra=''):
    return HttpResponse("Login or profile!")