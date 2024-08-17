from django.shortcuts import render,redirect
from django.template import Template
from django.http import HttpResponse
from .forms import main_form,Login
from django.views.decorators.cache import never_cache
from .models import main_model
# Create your views here.
def main(request):
    return render(request,template_name='index.htm')
@never_cache
def patient(request):
    url=request.build_absolute_uri()
    name=url.split('/')[-2]
    print(name)
    if request.method=='POST':
        r=request.POST.copy()
        if name=='doctors':
            r['user']=name
        form=main_form(r,request.FILES)
        if dict(form.data)['password']!=dict(form.data)['confirm_password']:
            form.add_error('confirm_password',"Please try to match the password string")
        print(dict(form.data)['username'])
        obj=main_model.objects.filter(username=dict(form.data)['username'][0],user=name)
        if len(list(obj.values()))!=0:
            form.add_error('username',"The username already exists")
        if form.is_valid():
            form.save()
            form_ins=form.instance
            obj=main_model.objects.get(username=form.cleaned_data['username'],user=name)
            return render(request,'dashboard.htm',{'obj':obj,'form_ins':form_ins})
        else:
            return render(request,'index.htm',{'form':form,'error':form.errors,'url':url})
    else:
        form=main_form()

    return render(request,'index.htm',{'form':form,'url':url})
@never_cache
def login(request):
    url=request.build_absolute_uri()
    name=url.split('/')[-2]
    print(name)
    if request.method=="POST":
        form=Login(request.POST)
        if form.is_valid():
            obj=main_model.objects.filter(username=dict(form.data)['username'][0],user=name,password=dict(form.data)['password'][0])
            if obj:
                obj=main_model.objects.get(username=dict(form.data)['username'][0],user=name)
                return render(request,'dashboard.htm',{'obj':obj})
            else:
                form.add_error(None,'check either username or password is wrong')
    else:
        form=Login()
    return render(request,'index.htm',{'login':form,'error':form.errors,'url':url[:-5]})
    