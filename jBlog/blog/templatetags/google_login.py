__author__ = 'Joran'
from django import template
from django.template import Library, Node, TemplateSyntaxError
register = template.Library()
link = """
<a class="zocial {0}" href="{1}">
    Login With Google
</a>
"""
urls={}
urls["googleplus"]="/oauth/google?next="
urls["facebook"]="#"
def buttn_txt(type="googleplus"):

    return link.format(type,urls[type])

def google_login_btn():
    return buttn_txt()
def fb_login_btn():
    return buttn_txt("facebook")
def bsocial():
    return "<div style='width:500px'>{0}{1}</div>".format(google_login_btn(),fb_login_btn())
register.simple_tag(google_login_btn)
register.simple_tag(fb_login_btn)
register.simple_tag(bsocial)