from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentREgistration
from .models import User

# Create your views here.

#this function will add new itme in data base
def add_show(request):
    if request.method == 'POST':
        fm = StudentREgistration(request.POST)
        if fm.is_valid():
            #fm.save()
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentREgistration()
    else :
        fm = StudentREgistration()
    stu = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stu})


# this for delete 
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#this for updata

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentREgistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentREgistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm,'id':id})

    





