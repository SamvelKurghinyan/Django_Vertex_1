from django.shortcuts import render
from .models import HomeBG, Post
from django.views.generic import ListView
# Create your views here.



class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        bg = HomeBG.objects.all()
        post = Post.objects.all()
        return render(request, self.template_name, {'bg':bg, 'post':post})