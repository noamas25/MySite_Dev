from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Todo
from .forms import TodoForm

@login_required(login_url="/admin/login/")
def index(request):
    tododata=Todo.objects.all()
    form=TodoForm(request.user)
    params={
        "login_user":request.user,
        "form":form,
        "tododata":tododata,

    }
    return render(request,"todolist/index.html",params)


    