from typing import Any
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .form import SessionForm,FriendForm,FindForm,CheckForm,MessageForm
from .models import Friend,Message
from django.db.models import QuerySet
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator


def __new__str__(self):
    result=""
    for item in self:
        result+="<tr>"
        for k in item:
            result+="<td>"+str(k)+"="+str(item[k])+"<td>"
        result+="</tr>"
    return result
QuerySet.__str__=__new__str__

def index(request,num=1):
    data=Friend.objects.all().order_by("age")
    page=Paginator(data,3)
    params={
        "title":"hello",
        "message":"",
        "data":page.get_page(num),
    }
    
    return render(request,"hello/index.html",params)

def create(request):
    
    if request.method=="POST":
        obj=Friend()
        friend=FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to="/hello")
    params={
        "title":"hello",
        "form":FriendForm(),
    }
    return render(request,"hello/create.html",params)

def edit(request,num):
    obj=Friend.objects.get(id=num)
    if request.method=="POST":
        friend=FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to="/hello")
    params={
        "title":"hello",
        "id":num,
        "form":FriendForm(instance=obj),
    }
    return render(request,"hello/edit.html",params)

def delete(request,num):
    friend=Friend.objects.get(id=num)
    if request.method=="POST":
        friend.delete()
        return redirect(to="/hello")
    params={
        "title":"hello",
        "id":num,
        "obj":friend,
    }
    return render(request,"hello/delete.html",params)

def find(request):
    if request.method=="POST":
        form=FindForm(request.POST)
        find=request.POST["find"]
        data=Friend.objects.filter(name__icontains=find)
        msg="結果:"+str(data.count())
    else:
        msg="search words..."
        form=FindForm()
        data=Friend.objects.all()
    params={
            "title":"Hello",
            "message":msg,
            "form":form,
            "data":data,        
            }
    return render(request,"hello/find.html",params)

def check(request):
    params={
        "title":"Hello",
        "message":"check Validation",
        "form":CheckForm(),
    }
    if request.method=="POST":
        form=CheckForm(request.POST)
        params["form"]=form
        if form.is_valid():
            params["message"]="OK"
        else:
            params["message"]="no good"
    return render(request,"hello/check.html",params)

def message(request,page=1):
    if request.method=="POST":
        obj=Message()
        form=MessageForm(request.POST,instance=obj)
        form.save()
    data=Message.objects.all().reverse()
    paginator=Paginator(data,5)
    params={
            "title":"Message",
            "form":MessageForm(),
            "data":paginator.get_page(page),

        }
    return render(request,"hello/message.html",params)




class FriendList(ListView):
    model=Friend

class FriendDetail(DetailView):
    model=Friend



def sample_middleware(get_response):

    def middleware(request):
        counter=request.session.get("counter",0)
        request.session["counter"]=counter+1
        response=get_response(request)
        print("count:"+str(counter))
        return response
    
    return middleware


#if "msg" in request.GET:
#        msg=request.GET["msg"]
#        result='you typed:"'+msg+'".'
#    else:
#        result="please send msg parameter!!"