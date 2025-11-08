
from django.urls import path
from posts import views
urlpatterns = [
    path('home/', views.home,name='home'),
    path("<int:id>/",views.post,name='post'),
    path("global/",views.global_page,name='global'),
]
