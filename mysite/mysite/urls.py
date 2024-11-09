from django.contrib import admin
from django.urls import path,include
import hello.views as hello
import login.views as login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/",include("hello.urls")),
    path("",login.index),
    path("sns/",include("sns.urls")),
    path("todolist/",include("todolist.urls")),
    path("api/",include("api.urls")),
    path("game/",include("game.urls")),
]
