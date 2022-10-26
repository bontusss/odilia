from random import randint
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.db.models import Q

from dictionary.models import Jargon

# Create your views here.
class HomePageView(View):
    def get(self, request, *args, **kwargs):
        featured_words = Jargon.objects.filter(status='active', visible=True, featured=True).order_by('category', '-created')[:5]
        random_words = Jargon.objects.filter(status='active', visible=True).order_by('category', 'created')
        count = Jargon.objects.count()
        words = Jargon.objects.all()[:3]
        # get one random word
        word_of_the_day = Jargon.objects.all()[randint(0, count - 1)]
        context = {
            'f_words': featured_words,
            'r_words': random_words,
            'daily_word': word_of_the_day,
            'words': words,
        }
        return render(request, 'index.html', context)



class SingleWordView(View):
    def get(self, request, id, *args, **kwargs):
        word = get_object_or_404(Jargon, id=id)
        word.visit_count = word.visit_count + 1
        word.save()
        related_words = Jargon.objects.filter(author=word.author).exclude(id=id).order_by('id')[:3]
        f_word = related_words.first()
        l_word  = related_words[1:]

        context= {
            'word': word,
            'r_words': related_words,
            'f_word': f_word,
            'l_word': l_word
        }
        return render(request, 'definition.html', context)