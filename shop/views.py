from django.shortcuts import render
from shop.models import Product ,Comment , Category


def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')


def products(request):
    category_filtering = request.GET.get('category')
    if category_filtering:
        products = Product.objects.filter(category=Category.objects.get(slug= category_filtering)).order_by(request.GET.get('ordering','pk'))
    else:
        products = Product.objects.all().order_by(request.GET.get('ordering','pk'))
        
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories':categories,
    }
    return render(request,'products.html',context)


def single_product(request,slug):
    product = Product.objects.get(slug=slug)
    comments = Comment.objects.filter(product_table=product,published=True)
    
    if request.method == 'POST':
            
            Comment.objects.create(
                user=request.POST['user'],
                email=request.POST['email'],
                comment_description=request.POST['message'],
                product_table = product
            )
            
    return render(request,'single-product.html',
                {'product': product,
                'comments':comments,
                })
