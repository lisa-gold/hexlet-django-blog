from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse, reverse_lazy


def index(request):
    return redirect(reverse('article',
                    kwargs={'tags': 'python', 'article_id': 42}))


def info(request, tags='test_tag', article_id=0):
    return render(
        request,
        'articles/index.html',
        context={'tags': tags, 'article_id': article_id}
    )
    

# class IndexView(View):
#     def get(self,request, *args, **kwargs):
#         return HttpResponse('article')
        # return render(
        #     request,
        #     'articles.index.html',
        #     context={'app_name': 'articles (app name)'}
        # )
