from django.conf.urls import url
from . import views


app_name = 'todo'
urlpatterns = [
    # ex: /todo/
    url(r'^$', views.index, name='index'),
    # ex: /todo/add
    url(r'^add', views.add, name='add'),
    #ex: /todo/delete/1
    url(r'^delete/(?P<todo_id>[0-9]+)$', views.delete, name='delete'),
    #ex: /todo/edit/1
    url(r'^edit/(?P<todo_id>[0-9]+)$', views.edit, name='edit'),
    url(r'^update/(?P<todo_id>[0-9]+)$', views.update, name='update'),
]