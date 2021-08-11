from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

# API endpoints
urlpatterns = format_suffix_patterns(
    [
        path("core/", views.PostList.as_view(), name="post-list"),
        path("core/<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
    ]
)
