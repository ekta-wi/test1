from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    filtered_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': filtered_posts})

#View details of the exisitng posts
def post_detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post_detail})

#Create a new post
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        #Validate the form
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # To redirect to the post detail (static) page
            return redirect('post_detail', pk=post.pk)
    else:
        # Form is opened in view status. Display an empty form
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#Edit an existing post
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # To redirect to the post detail (static) page containing the edited post's data
            return redirect('post_detail', pk=post.pk)
    else:
        # Form is opened in view status. Display an empty form
        # The get post is passed onto the form
        form = PostForm(instance=post)
    #Render empty post new form
    return render(request, 'blog/post_edit.html', {'form': form})
