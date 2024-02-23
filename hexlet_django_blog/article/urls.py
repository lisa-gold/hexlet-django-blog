from django.urls import path
from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    # path('', views.index),
    path('<int:id>', views.ArticleView.as_view(), name='article_view'),
    path('<int:article_id>/comments/<int:id>/', views.ArticleCommentsView.as_view()),
]
