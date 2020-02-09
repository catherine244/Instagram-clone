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
    
class PostCreateView(LoginRequiredMixin,CreateView):
    form_class = PhotoUploadModelForm
    template_name = 'instagram/image_upload.html'
 
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.user_profile= self.request.user.profile
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Image
    fields = ['title', 'content']   
    
class create_comment(CreateView):
    model=Comment
    template_name= 'instagram/image_list.html' 
    
    context_object_name = 'comments'
    ordering = ['-posted_on']

def signout(request):
    logout(request)
    return redirect('logi     
        
def add_comment(request,post_id):
    post = get_object_or_404(Image, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
    return redirect('home')
    
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_user = Profile.search_by_username(search_term)
        message = f"{search_term}"
        context = {
            'message': message,
            'searched_user': searched_user
        }
        return render(request, 'search.html', context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'index.html',{"message":message})
    