from django.shortcuts import render

# Create your views here.

def Blog_List(request):
    return render(request, 'App_Blog/blog_list.html', context={})
