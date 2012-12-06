# Create your views here.
from django.http import  HttpResponse, HttpResponseForbidden
from django.shortcuts import  render_to_response#,RequestContext
from jBlog import  settings
import os
def index(ref,folder,file_base):
    folder_path = os.path.join(settings.PROJECT_PATH,"..",folder)
    if not os.path.exists(folder_path):
        return HttpResponse("%s not found"%folder_path)
        return HttpResponseForbidden()
    src_doc = os.path.join(folder_path,file_base+".txt")

    if not os.path.exists(src_doc):
        return HttpResponse("%s not found"%src_doc)
    html_path = os.path.join(folder_path,file_base+".html")
    try:
        if os.path.getmtime(src_doc) > os.path.getmtime(html_path):
            raise Exception("Remake File")
    except:
        os.system("asciidoc.py --out-file=\"%s\" --no-header-footer \"%s\""%(html_path,src_doc))

    ctx={"entry":open(html_path).read(),"css_files":["/media/css/asciidoc.css"]}
    return render_to_response('asciidoc_templates/view.html',ctx)#,context_instance=RequestContext(ref))
