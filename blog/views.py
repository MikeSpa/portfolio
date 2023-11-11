from blog.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# def blog(request):
#     return render(request, "blog/blog.html", {})


class BlogList(ListView):
    model = Post


class BlogDetail(DetailView):
    model = Post
