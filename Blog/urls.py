from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    About,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    # UserPostListView
)

urlpatterns = [
    path('', BlogListView.as_view() , name = "blog-home" ),
    path('blog/<int:pk>/', BlogDetailView.as_view() , name = "blog-detail" ),
    # path('user/<str:username>/', UserPostListView.as_view(), name= "user-posts" ),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view() , name = "blog-update" ),
    path('blog/new/', BlogCreateView.as_view() , name = "blog-create" ),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view() , name = "blog-delete" ),
    path('about/', About , name = "blog-about" ),
]