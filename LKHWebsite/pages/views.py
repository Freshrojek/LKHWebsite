from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article, Author


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 321, 111],
    }

    return render(request, "about.html", my_context)

def vue_test(request):
    return render(request, 'vueTest.html')

def blogView(request):
    return render(request, "home.html", {})
def frontend(request, slug=None):
    articles = Article.objects.all()
    authors = Author.objects.all()

    data = {
        'articles': articles,
        'authors': authors,
    }

    return render(request, 'blogTemplate.html', data)


# def vueT_test(request):
#     return render(request, 'vuetifyTest.html')
