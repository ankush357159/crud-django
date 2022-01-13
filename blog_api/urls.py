from django.urls import path

from blog_api.views import function_views

urlpatterns = [
    # Function based views
    path('posts/', function_views.post_lists),
    path('posts/<str:id>', function_views.post_details),
]