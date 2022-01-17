from django.urls import path
from blog_api.views import function_views
from blog_api.views.class_based_views import PostDetails, PostLists
from blog_api.views.generic_views  import MyTokenObtainPairView, PostDetail, CategoryDetail, PostListView, CategoryListView, UserCreateView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Function based views
    path('posts/', function_views.post_lists),
    path('posts/<str:id>/', function_views.post_details),

    # Class based views
    path('blog_posts/', PostLists.as_view()),
    path('blog_post/<str:id>/', PostDetails.as_view(), name='post_detail'),

    # Generic class based views
    path('category/', CategoryListView.as_view()),
    path('category/<str:pk>/', CategoryDetail.as_view()),
    path('post/', PostListView.as_view()),
    path('post/<int:pk>/',PostDetail.as_view()),

    # User urls
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="logout"),
    path('register_user/', UserCreateView.as_view())

]