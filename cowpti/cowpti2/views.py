from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django import forms
from cowpti2.images_manipulation import genererVersions

class UploadFileForm(forms.Form):
    file = forms.FileField()

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            genererVersions(request.FILES['file'].name)
            return HttpResponseRedirect('http://46.105.155.86/5a731cb7f8/index.html')
    raise Http404
