from django.urls import path

from . import views

app_name = "sistema"

urlpatterns = [
    path('', views.index, name='index'),

    # Gerente
    path('solicitacoes/<int:pagina>/', views.solicitacoes, name='solicitacoes'),
    path('solicitacoes/', views.solicitacoes, name='solicitacoes'),

    path('<int:funcionario_id>/aprovar',
         views.ver_funcionario_aprovar, name='ver_aprovar'),
    path('solicitacoes/<int:funcionario_id>/aprovar/',
         views.ver_funcionario_aprovar, name='aprovar'),

    path('funcionarios/<int:pagina>/',
         views.ver_funcionarios, name='funcionarios'),
    path('funcionarios/', views.ver_funcionarios, name='funcionarios'),
    path('<int:funcionario_id>/excluir/',
         views.funcionario_excluir, name='ver_excluir'),
    path('funcionarios/<int:funcionario_id>/excluir/',
         views.funcionario_excluir, name='excluir'),

]
