from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns=[
    #path("",views.index,name="index"),
    path("todo/",views.todo,name="todo"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login_view,name="login"),
    #path("logout",LogoutView.as_view(),name="logout"),
    path("logout/",views.logout_view, name="logout"),
    path("delete/<int:todo_id>/",views.deletetodo,name="delete"),
    path("update/<int:todo_id>/",views.updatetodo, name="update"),
    path("done/<int:todo_id>/",views.donetodo, name="done"),
    path("viewdone/",views.viewdone, name="viewdone"),

]