from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class BookmarkView(TemplateView):
    template_name = ""