from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
urlpatterns = [

    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$',views.profile, name='profile'),
    url(r'^edit/$',views.edit_profile,name='edit profile'),
    url(r'^change-password/$',views.change_password,name='change password'),
    #url(r'^post_view/$',view.post_view,{'template_name': 'accounts/post_list.html'}),
    ]