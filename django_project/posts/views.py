from django.views.generic import ListView, TemplateView
from .models import Post
    
class HomePageView(ListView):
    model = Post
    template_name = "home.html"
class AboutPageView(TemplateView): # new
    template_name = "about.html"