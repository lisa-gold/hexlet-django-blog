from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.urls import reverse, reverse_lazy

from hexlet_django_blog.article.models import Article


# def index(request):
#     return redirect(reverse('article',
#                     kwargs={'tags': 'python', 'article_id': 42}))


class IndexView(View):

    def get(self, request, *args, **kwargs):
        # return HttpResponse('article')
        articles = Article.objects.all()[:15]
        return render(
            request,
            'articles/index.html',
            context={'articles': articles}
        )


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/show.html',
            context={'article': article}
        )


class ArticleCommentsView(View):

    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs['id'], article_id=kwargs['article_id'])
        return render(
            request,
            'articles/comments.html',
            context={'comment': comment}
        )
