from django.urls import path
from .views import NewsListView, NewsDetailView, DashboardView, CreatePostView, PostDeleteView, PostUpdateView, \
    SearchView, BangladeshListView, BusinessListView, SportsListView, LifestyleListView, TechListView,ShowbizListView

urlpatterns = [
    path('', NewsListView.as_view(), name='list-page'),
    path('dashboard/', DashboardView.as_view(), name='dashboard-page'),
    path('new-post/', CreatePostView.as_view(), name='new-post-page'),
    path('<slug:slug>', NewsDetailView.as_view(), name='list-detail'),
    path('<slug:slug>/delete', PostDeleteView.as_view(), name='post-delete-page'),
    path('<slug:slug>/edit', PostUpdateView.as_view(), name='post-update-page'),
    path('search/', SearchView.as_view(), name='search-page'),
    path('bangladesh/', BangladeshListView.as_view(), name='bangladesh-page'),
    path('business/', BusinessListView.as_view(), name='business-page'),
    path('sports/', SportsListView.as_view(), name='sports-page'),
    path('lifestyle/', LifestyleListView.as_view(), name='lifestyle-page'),
    path('technoligy/', TechListView.as_view(), name='technology-page'),
    path('showbiz/', ShowbizListView.as_view(), name='shobiz-page'),
    # path('<slug:slug>/Comment', CommentCreateView.as_view(), name='comments-page'),
]
