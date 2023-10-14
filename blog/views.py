from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def index(request):
    post_list = Post.objects.order_by('-create_date')
    context = {'posts': post_list}
    return render(request, 'blog/post_list.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post':post}
    return render(request, 'blog/post_detail.html', context)

def comment_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('blog:detail', post_id=post_id)

def post_create(request):
    form = PostForm()
    context = {'form':form}
    return render(request, 'blog/post_form.html', context)
