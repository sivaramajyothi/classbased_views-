from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView

# Create your views here.
from app.forms import *

#fBV for dealing with django forms
def fbv_string(request):
    return HttpResponse('<h1>This is returned by FBV<h1>')
#CBV forreturning string as response

class cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>This is returned by CBV<h1>')
    
#fbv for returning html page 
def fbv_page(request):
    return render(request,'fbv_page.html')

#cbv for returning html page
class cbv_page(View):
    def get(self,request):
        return render(request,'cbv_page.html')
#fbv for dealing with django forms

def fbv_form(request):
    form=StudentForm()
    d={'form':form}

    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'fbv_form.html',d)

#cbv for dealing with django forms
class cbv_form(View):
    def get(self,request):
        form=StudentForm()
        d={'form':form}
        return render(request,'cbv_form.html',d)
    def post(self,request):
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))

#by using templateview class returning html page
class cbv_template(TemplateView):
    template_name='cbv_template.html'      
