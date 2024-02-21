from django.urls import path
from hexlet_django_blog.article import views


urlpatterns = [
    # path('', views.IndexView.as_view()),
    path('', views.index),
    path('<tags>/<int:article_id>', views.info, name='article'),
]
