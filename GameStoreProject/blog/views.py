from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def post_list(request):
    post_list = Post.objects.all().order_by('-pub_date')
    per_page = request.GET.get('per_page', 10)
    paginator = Paginator(post_list, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'per_page': per_page})