from django.urls import path
from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleFormCreateView


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    # path('', views.index),
    path('<int:id>', views.ArticleView.as_view(), name='article_view'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create')
]
