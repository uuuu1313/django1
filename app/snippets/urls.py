from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()), # CBV
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()), # CBV
    # path('snippets/', views.snippet_list), # FBV
    # path('snippets/<int:pk>/', views.snippet_detail), # FBV
]

urlpatterns = format_suffix_patterns(urlpatterns)   # URL 패턴에 포맷 접미사를 추가하기 위해 사용