from django.shortcuts import render_to_response,HttpResponse,redirect
from django.core.context_processors import csrf
from django.utils.html import escape
import re,time,urllib,urllib2
from django.db.models import Q
import json
from django.template import RequestContext
from models import Entry,Tag,Comment
def index(request,path=''):
    return render_to_response('blog/list.html', 
                              {'entries':
                                Entry.objects.all().order_by("publish_date").reverse()[:5]})
def search(request,path=''):
    def __no_qry():
         return HttpResponse("No Query!")
    def parse_query(qstring):
        if not qstring:
            return None
        d = {'tags':[],'words':[],'exclude':[]}
        for q in qstring.split():
            q  = q.strip()
            if q.startswith("[") and q.endswith("]"):
                d["tags"].append(q[1:-1])
            elif q.startswith("-"):
                d['exclude'].append(q[1:])
            elif q:
                d["words"].append(q)
        return d
    def _get_posts(tags,words,excepts):
        objs = Entry.objects
        tag_ids = [o.id for t in tags for o in Tag.objects.filter(title=t) ]
        qset1 = Q()
        for idx in tag_ids:
            qset1 |= Q(tags = idx)
        qset = Q()
        for term in words:
            qset |= Q(title__contains=term)
            qset |= Q(body__contains =term)
        objs = objs.filter(qset1, qset)

        return objs.order_by('publish_date')


    def get_posts(search_string):
        d = parse_query(search_string)
        if not d:
            return None
        excludes,tags,words = map(lambda k:d[k],sorted(d.keys()))
        return _get_posts(tags,words,excludes)
    if 'q' not in request.GET:
        return __no_qry()
    result = get_posts(request.GET['q'])

    if not result:
        return __no_qry()
    return render_to_response('blog/list.html', {'entries':result})

def upload_image(requesst,path=''):
    return HttpResponse("Complete")

def view(request,article_id=-1):

    try:article = Entry.objects.get(pk=article_id)
    except ValueError:
        article = Entry.objects.get(title=article_id.replace("_"," "))
    ctx = {'entry':article,'title':article.title}
    ctx.update(csrf(request))
    return render_to_response('blog/view.html',ctx,context_instance=RequestContext(request))
def add_comment(request,article_id):
    try:
        article = Entry.objects.get(pk=article_id)
    except:
        return HttpResponse("Article Not Found!")
    #c = Comment(author=)
    p = article_id
    c=Comment(post = article,body =request.POST['body'],author=request.POST['author'],timestamp=time.strftime("%Y-%m-%d %H:%M"))
    c.save()
    return redirect("/view/%s"%p)
