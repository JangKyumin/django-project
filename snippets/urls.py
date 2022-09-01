from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view()),
    # path('', views.snippet_list),
    # path('<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
