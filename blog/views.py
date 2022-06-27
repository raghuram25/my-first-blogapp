from django.shortcuts import render
from .models import Post  #Post is a class which we created in models.py which has datatype declared
from django.utils import timezone #To display our blogs based on published date
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})