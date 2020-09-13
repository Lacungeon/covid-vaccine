from django.views.generic import View
from django.shortcuts import render
import requests

class IndexView(View):
    def get(self, request):
        data = requests.get('http://newsapi.org/v2/everything?q=COVID VACCINE&sortBy=popularity&apiKey=56d9abf8763641d49312b68ad72a9d4a').json()
        context = {}
        context['articles'] = data['articles']
        return render(request, 'index.html', context)