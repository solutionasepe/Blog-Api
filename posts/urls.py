from django.urls import path, include
from . import views

from rest_framework.routers import SimpleRouter

routers = SimpleRouter()
routers.register('users', views.UserViewSet, basename="userview")
routers.register('', views.PostViewSet,)



# urlpatterns = [
#     # path("posts", views.PostList.as_view()),
#     # path("posts/<int:pk>/", views.PostDetail.as_view()),
#     path('posting/', views.Posting, name='post')
# ]

urlpatterns = [
               path('Example/', views.Exampleview.as_view(), name="Exampleview"),
               ]+ routers.urls

