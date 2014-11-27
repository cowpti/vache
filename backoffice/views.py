from django.shortcuts import render_to_response
from django.template import RequestContext
from upload.models import Picture

def home(request):
    return render_to_response('index.html',context_instance=RequestContext(request))
def submit(request):
    if request.method == 'POST':
        pic=request.FILES.get('myFile')
        profile_obj=Picture(profile_picture=pic).save()
    return render_to_response('index.html',context_instance=RequestContext(request))