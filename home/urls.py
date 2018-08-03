from django.conf.urls import url
from home.views import HomeView
#from home.views import CommentView
#from .views import views
#HomeView ,post_view

urlpatterns = [

    url(r'^$', HomeView.as_view(), name='home'),
    #url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^comment/$', HomeView.as_view(), name='add_comment_to_post'),

]