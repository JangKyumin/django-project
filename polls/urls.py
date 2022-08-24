from django.urls import path

from . import views

'''
    path에 들어가는 converter는 int, path, slug, str, uuid를 사용 가능하다.
'''
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
