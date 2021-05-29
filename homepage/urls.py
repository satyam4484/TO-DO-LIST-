from django.urls import path
from . import views 

urlpatterns = [
    path('',views.usersignup,name='signup'),
    path('profile/',views.profile,name = 'profile'),
    path('logout/',views.userlogout,name='logout'),
    path('login/',views.user_login,name='login'),
    path('update/<int:id>',views.edit,name='update'),
    path('task/',views.addtask,name='task'),
    path('view/<int:id>',views.viewdata,name='viewdata'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('done/<int:id>',views.done,name='done'),
]
