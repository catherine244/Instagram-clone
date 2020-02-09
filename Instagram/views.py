# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    posts= Image.objects.all(),
    commentform= CommentForm()
    
    return render(request, 'index.html', locals())

class PostListView(LoginRequiredMixin,ListView):
    model=Image
    template_name= 'instagram/image_list.html' # <app>/<model>_<view_type>.html
    
    context_object_name = 'posts'
    ordering = ['-time_created']
