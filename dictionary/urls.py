

from django.urls import path

from dictionary.views import HomePageView, SearchResultsView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("search/", SearchResultsView.as_view(), name='search-results')
]
