from django.conf.urls import url
from . import views


app_name = 'todo'
urlpatterns = [
    # ex: /todo/
    url(r'^$', views.index, name='index'),
    # ex: /todo/add
    url(r'^add', views.add, name='add'),
    #ex: /todo/delete
    # url(r'^delete', views.delete, name='delete'),
    #ex: /polls/5/vote
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]