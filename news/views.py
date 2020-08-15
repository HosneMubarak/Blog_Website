from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from .models import NewsCategory, NewsModel, CommentModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from datetime import datetime


class SearchView(ListView):
    model = NewsModel
    context_object_name = 'search_list'
    template_name = 'news/search_list.html'

    def get_queryset(self):
        titel = self.request.GET.get('title_q')
        return NewsModel.objects.filter(
            Q(text__icontains=titel)
        )


class NewsListView(ListView):
    model = NewsModel
    context_object_name = 'news_list'
    template_name = 'news/news_list.html'


class NewsDetailView(DetailView):
    model = NewsModel
    context_object_name = 'news_details'
    template_name = 'news/news_detail.html'


class DashboardView(LoginRequiredMixin, ListView):
    model = NewsModel
    post = NewsModel.objects.all()
    template_name = 'news/dashboard.html'

    def get_queryset(self):
        return NewsModel.objects.filter(author=self.request.user)


class CreatePostView(LoginRequiredMixin, CreateView):
    model = NewsModel
    fields = [
        'title', 'category', 'text', 'image1', 'image2'
    ]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(CreatePostView, self).form_valid(form)

    template_name = 'news/create_post.html'
    success_url = reverse_lazy('dashboard-page')


class PostDeleteView(DeleteView):
    model = NewsModel
    template_name = 'news/delete_post.html'
    success_url = reverse_lazy('list-page')


class PostUpdateView(UpdateView):
    model = NewsModel
    fields = [
        'title', 'category', 'text', 'image1', 'image2'
    ]
    template_name = 'news/post-update.html'
    success_url = reverse_lazy('dashboard-page')


# class CommentCreateView(CreatePostView):
#     model = CommentModel
#     fields = [
#         'comment_text',
#     ]
#     template_name = 'news/comment_create.html'
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.author = self.request.user
#         self.object.save()
#         return super(CommentCreateView, self).form_valid(form)


class BangladeshListView(ListView):
    model = NewsModel
    context_object_name = 'news_list'
    template_name = 'news/bdlist.html'

    def get_queryset(self):
        news_list = NewsModel.objects.filter(category__category_name='BANGLADESH')
        return news_list


class BusinessListView(ListView):
    model = NewsModel
    context_object_name = 'news_list'
    template_name = 'news/bussonesslist.html'

    def get_queryset(self):
        news_list = NewsModel.objects.filter(category__category_name='BUSINESS')
        return news_list


class SportsListView(ListView):
    model = NewsModel
    context_object_name = 'news_list'
    template_name = 'news/sportslist.html'

    def get_queryset(self):
        news_list = NewsModel.objects.filter(category__category_name='SPORTS')
        return news_list


class LifestyleListView(ListView):
    model = NewsModel
    context_object_name = 'news_list'
    template_name = 'news/lifestylelist.html'

    def get_queryset(self):
        news_list = NewsModel.objects.filter(category__category_name='LIFESTYLE')
        return news_list


class TechListView(ListView):
    model = NewsModel
    context_object_name = 'news_list'
    template_name = 'news/techlist.html'

    def get_queryset(self):
        news_list = NewsModel.objects.filter(category__category_name='TECHNOLOGY')
        return news_list


class ShowbizListView(ListView):
    model = NewsModel
    context_object_name = 'news_list'
    template_name = 'news/showbizlist.html'

    def get_queryset(self):
        news_list = NewsModel.objects.filter(category__category_name='SHOWBIZ')
        return news_list
