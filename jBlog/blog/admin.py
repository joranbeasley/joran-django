from django.contrib import admin
from models import Entry,Category,Tag
from django import forms

class KindEditor(forms.Textarea):
    class Media:
       css ={'all':['/media/kindeditor-4.1.2/themes/default/default.css']}
       
       js = ( '/media/kindeditor-4.1.2/kindeditor-min.js', '/media/kindeditor-4.1.2/lang/en.js',)
    def __init__(self):
       attrs = {}
       attrs['class'] = 'kindeditor'
       super(KindEditor, self).__init__(attrs)

class EntryAdminForm(forms.ModelForm):
  class Meta:
     model = Entry
     widgets = {
        'body':KindEditor()
     }

class EntryAdmin(admin.ModelAdmin):
    #fields = ('category','title', 'body','publish_date')
    form = EntryAdminForm
admin.site.register(Entry, EntryAdmin)



admin.site.register(Category)
admin.site.register(Tag)
