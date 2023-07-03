from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models import customer
from store.models.customer import Customer
from store.models.cart import Cart as cart
from django.views import  View
from store.models.product import Products
from django.contrib import messages

class Cart(View):
    # def get(self , request):
    #     ids = list(request.session.get('cart').keys())
    #     products = Products.get_products_by_id(ids)
    #     print(products)
    #     return render(request , 'cart.html' , {'products' : products} )
    
    def get(self, request):
        userid = request.session.get('customer')
        print(userid)


        customer = Customer.objects.get(id=userid)
        print(customer)

        carts = cart.objects.filter(user=customer)
        print(carts)
        
        product_ids = list(carts.values_list('product_id', flat=True))
        print(product_ids,'productids')

        products = Products.objects.filter(id__in=product_ids)
        print(products)
        
        for product in products:
            print(product.name)
            
            
        context = {'products': products}
        return render(request, 'cart.html', context)    
    # def post(self, request):
        
    #     return redirect('cart')  
    






