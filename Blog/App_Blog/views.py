import imp
from urllib import request
import uuid
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponsePermanentRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Blog.models import Blog, Comment, Likes
from App_Blog.forms import CommentForm

# Create your views here.

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = 'App_Blog/create_blog.html'

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('App_Blog:my_blogs'))



class EditBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = 'App_Blog/edit_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Blog:blog_details', kwargs={'slug':self.object.slug})
    


class DeleteBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Blog:blog_details')

def delete_blog(request, pk):
    obj = Blog.objects.get(pk=pk)
    if obj.author == request.user:
        obj.delete()
        return HttpResponseRedirect(reverse('App_Blog:my_blogs'))
    else:
        return HttpResponse("Bad request 404")


class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = 'App_Blog/my_blogs.html'
  

@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug = slug)
    form  = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug': slug}))
    
    return render(request, 'App_Blog/blog_details.html', context={'blog': blog, 'form':form})


