

from django.urls import path

from dictionary.views import HomePageView, SingleWordView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path('word/<int:id>/', SingleWordView.as_view(), name="definition")
]
