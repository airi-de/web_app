from django.views.generic import ListView,DetailView
from django.views.generic.base import TemplateView
from .models import BlogPost

class IndexView(ListView):
    model=BlogPost
    template_name='seisaku/index.html'
    context_object_name='posts'
    ordering=['-posted_at']
    paginate_by=1

class AboutView(TemplateView):
    templete_name="seisaku/about.html"

class ContactView(TemplateView):
    template_name="seisaku/contact.html"