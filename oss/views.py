from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('-updated_date')
    return render(request, 'oss/article_list.html', {'articles': articles})