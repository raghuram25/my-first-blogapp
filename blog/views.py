from django.shortcuts import render, get_object_or_404 #incase there are no posts we get this error (error handling)
from .models import Post                               #Post is a class which we created in models.py which has datatype declared
from django.utils import timezone
from .forms import PostForm                            #To display our blogs based on published 

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

from django.shortcuts import redirect                      #after getting data from forms and on click of save , it will redirect to post_detail view(original page)
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#The above two "post_new" functions , the first one is called upon click of 'new post' button. So if we try to click Save without filling any data
#it is again calling the form = Postform() in the else block...So only same page is reloaded. if post is valid ...that means if we type something
#according to Validity it will be save (post.save())


def post_edit(request, pk):                                        #postedit feature for existing posts
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})