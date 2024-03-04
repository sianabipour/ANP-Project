from django.shortcuts import render 
from blog.models import Category ,Blog ,Comment,Tag



def blogs(request):
    category = Category.objects.all()
    blogs = Blog.objects.all()
    context = {
        'category':category,
        'blogs':blogs,
    }
    return render(request,'blogs.html',context)

def single_blog (request,slug) :
    tags = Tag.objects.all()
    article = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(blog=article,published=True)
    suggested_blogs = Blog.objects.filter(category=article.category).exclude(slug=slug)[:5]
    latest = Blog.objects.all().order_by("-date_create")[:3]
    
    if request.method == 'POST':
        
        Comment.objects.create(
            user=request.POST['user'],
            email=request.POST['email'],
            comment_description=request.POST['message'],
            blog = article
        )
    
    context= {
        'article': article,
        'comments':comments,
        'latest':latest,
        'suggested_blogs':suggested_blogs,
        'tags':tags,
        }
        
    return render(request,'single-blog.html',context)
