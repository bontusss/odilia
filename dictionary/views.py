from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from dictionary.models import Definition, Word

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


class SearchResultsView(ListView):
    model = Definition
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        # object_list = Word.objects.filter(Q(name__icontains=query | Q(definition__meaning__icontains=query)))
        object_list = Definition.objects.filter(Q(word__name__icontains=query) | Q(meaning__icontains=query))
        return object_list