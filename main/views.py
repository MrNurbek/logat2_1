from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View

from .models import Word


class HomePageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        return context


def homePageView2(request, id):
    dict = {
        "word": Word.objects.get(id=id),
        "count": Word.objects.all().count()
        # "word_list": Word.objects.filter(Q(name=Word.objects.get(id=id).name))
    }
    return render(request, 'index.html', context=dict)


class HomePageView2(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.get(id=self.kwargs.id)
        context['countWords1'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        render(context, 'index.html')


class HomePageView3(TemplateView):
    template_name = 'index2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        return context


class HomePageView0(TemplateView):
    template_name = 'loyiha.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        return context


class HomePageView02(TemplateView):
    template_name = 'saytlar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        return context

class HomePageView01(TemplateView):
    template_name = 'foydalanish.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        return context


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    return render(request, 'about.html')


class SearchResultsView(ListView):
    model = Word
    template_name = 'main/index.html'

    # extra_context = {'title': 'Bosh sahifa', 'countWords': Word.objects.all().count()}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Word.objects.filter(Q(name=query))
        return object_list


class SearchResultsView2(ListView):
    model = Word
    template_name = 'index.html'

    # extra_context = {'title': 'Bosh sahifa', 'countWords': Word.objects.all().count()}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        return context

    # def get_queryset(self):
    #     query = self.request.GET.get("q")
    #     object_list = Word.objects.filter(Q(name=query))
    #     return object_list
    def get_queryset(self):
        name = self.request.GET.get("q")
        return Word.objects.filter(
            Q(name__icontains=name)
        )


class SearchResultsView3(ListView):
    model = Word
    template_name = 'index2.html'

    # extra_context = {'title': 'Bosh sahifa', 'countWords': Word.objects.all().count()}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        return context

    # def get_queryset(self):
    #     query = self.request.GET.get("q")
    #     object_list = Word.objects.filter(Q(name=query))
    #     return object_list
    def get_queryset(self):
        name = self.request.GET.get("q")
        return Word.objects.filter(
            Q(name__icontains=name)
        )


class SearchResultsList(ListView):
    model = Word
    context_object_name = "words"
    template_name = "index2.html"

    def get_queryset(self):
        name = self.request.GET.get("q")
        return Word.objects.filter(
            Q(name__icontains=name))

# server {
#     listen 80;
#     server_name gippologik-termin.uz;
#
#     location = /favicon.ico { access_log off; log_not_found off; }
#     location /static/ {
#         root /home/ubuntu/nurbek/djangodictionary
# ;
#     }
#
#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/run/sayt.sock;
#     }
# }
