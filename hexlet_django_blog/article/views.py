from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages import get_messages

from hexlet_django_blog.article.models import Article
from .forms import ArticleForm


MESSAGE_TAGS = {
    messages.INFO: "",
    50: "critical",
}

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


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request,
            'articles/create.html',
            {'form': form}
        )
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/articles/')
        messages.add_message(request, messages.INFO, "too short")
        messages_list = get_messages(request)
        return render(
            request,
            'articles/create.html',
            {'form': form, 'messages': messages_list}
        )


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        messages.add_message(request, messages.INFO, "error, try again")
        messages_list = get_messages(request)
        if form.is_valid():
            form.save()
            return redirect('/articles/')
        
        return render(
            request,
            'articles/update.html',
            {'form': form, 'article_id':article_id, 'messages': messages_list})

class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles_index')
