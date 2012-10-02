__author__ = 'Joran'
import urllib2,urllib
import json

from jBlog import settings


def get_token(code=None):
    # The client id and secret can be found on your API Console.
    # The client id and secret can be found on your API Console.
    CLIENT_ID = settings.GOOGLE_AUTH_SETTINGS['client_id']
    CLIENT_SECRET = settings.GOOGLE_AUTH_SETTINGS['client_secret']

    # Authorization can be requested for multiple APIs at once by specifying multiple scopes separated by # spaces.
    SCOPES = settings.GOOGLE_AUTH_SETTINGS['scopes']
    USER_AGENT = 'adventuresinpy'

    # Save the token for later use.
    token = dict(
        scope=' '.join(SCOPES),client_id=CLIENT_ID,
        user_agent=USER_AGENT,redirect_uri=settings.GOOGLE_AUTH_SETTINGS['redirect_url'])
    if code:
        token['client_secret']=CLIENT_SECRET
        token['code']=code
        token['grant_type']="authorization_code"
    else:
        token['response_type']='code'

    return token
def sendToken(url,tok,json=False):
    #path='https://accounts.google.com/o/oauth2/token'
    req=urllib2.Request(url, urllib.urlencode(tok))
    req.add_header("Content-type", "application/x-www-form-urlencoded")
    return urllib2.urlopen(req).read()
    # The redirect_url parameter needs to match the one you entered in the API Console and points
    # to your callback handler.
    #return redirect(
    #    token.generate_authorize_url(redirect_uri='http://127.0.0.1:8000/oath_callback'))

def validate(token):
    return json.loads(urllib2.urlopen("https://www.googleapis.com/oauth2/v1/tokeninfo?access_token="+token).read())
def UserData(token):
    return json.loads(urllib2.urlopen("https://www.googleapis.com/oauth2/v1/userinfo?access_token="+token).read())
def oauth(request,option=''):

    code = request.GET['code']

    token = get_token(code)
    result = sendToken('https://accounts.google.com/o/oauth2/token',token)

    token_data = json.loads(result)




    return redirect(request.session.pop('last_url'))
    # )
    #result should be json that has token info
    #xyz = token.get_access_token(code)
    #path='https://accounts.google.com/o/oauth2/auth'
    #return HttpResponse(path+mydata)
    #req=urllib2.Request(path, mydata)
    #return HttpResponse(str(req.data))
    #req.add_header("Content-type", "application/x-www-form-urlencoded")
    #page=urllib2.urlopen(req).read()
    return HttpResponse(str(token_data)+"asd")
    #json_o = js
    #return render_to_response('blog/authorize_code.html',{'code':code}