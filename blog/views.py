from django.shortcuts import redirect, render

from .forms import CommentForm
from .models import Post

# Create your views here.
def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    form = CommentForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
        else:
            form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})