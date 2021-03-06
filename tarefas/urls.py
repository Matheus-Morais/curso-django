from django.conf.urls import url

from . import views
app_name = "tarefas"
urlpatterns = [
    url('^categoria/$', views.lista_categoria, name = 'categoria'),
    url('^nova-categoria/$', views.nova_categoria, name = 'nova-categoria'),
    url('^delete-categoria/(?P<id>[0-9]+)/$', views.delete_categoria, name = 'delete-categoria'),
    url('^update-categoria/(?P<id>[0-9]+)/$', views.update_categoria, name = 'update-categoria'),
    url('^nova-tarefa/$', views.nova_tarefa, name = 'nova-tarefa'),
    url('^lista-tarefa/$', views.lista_tarefa, name = 'lista-tarefa'),
    url('^delete-tarefa/(?P<id>[0-9]+)/$', views.delete_tarefa, name = 'delete-tarefa'),
    url('^update-tarefa/(?P<id>[0-9]+)/$', views.update_tarefa, name = 'update-tarefa'),
    url('^detalhes-tarefa/(?P<id>[0-9]+)/$', views.detalhes_tarefa, name = 'detalhes-tarefa'),
    url('^buscar/$', views.search, name = 'search'),
]