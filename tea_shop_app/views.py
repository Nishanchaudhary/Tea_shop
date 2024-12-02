from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product,Tea

def base(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing to our newsletter!")
            return redirect('home')  # Replace 'home' with the name of your desired route
        else:
            messages.error(request, "Invalid email address. Please try again.")
    else:
        form = NewsletterForm()
    return render(request, 'layout/base.html', {'form': form})


def index(request):
    
    return render(request,'index.html')

def product_list(request):
    products = Product.objects.all()  
    return render(request, 'shop.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.views += 1
    product.save()
    return render(request, 'product_detail.html', {'product': product})


@login_required
def like_product(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        
        if request.user in product.liked_by.all():
            # Unlike the product
            product.liked_by.remove(request.user)
            product.likes -= 1
            liked = False
        else:
            # Like the product
            product.liked_by.add(request.user)
            product.likes += 1
            liked = True
        
        product.save()
        return JsonResponse({"likes": product.likes, "liked": liked})
    return JsonResponse({"error": "Invalid request"}, status=400)

def search_products(request):
    query = request.GET.get('q', '')  # Get the search query
    products = Product.objects.filter(name__icontains=query) if query else Product.objects.all()

    context = {
        'query': query,
        'products': products,
    }
    return render(request, 'product_search.html', context)

def about(request):
    return render(request, 'about.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def blog(request):
    teas = Tea.objects.all()
    return render(request, 'blog.html', {'teas': teas})

def blog_detail(request, pk):
    tea = get_object_or_404(Tea, pk=pk)
    return render(request, 'blog_detail.html', {'tea': tea})