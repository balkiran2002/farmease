from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item

def add_item(request):
    if request.method == 'POST':
        # Get data from the form
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        seasons = request.POST.get('seasons')
        crops = request.POST.get('crops')
        soil_type = request.POST.get('soil_type')
        photo = request.FILES.get('photo') 
        description = request.POST.get('description') # For file uploads

        # Save the data to the database
        item = Item(
            product_id=product_id,
            product_name=product_name,
            category=category,
            price=price,
            quantity=quantity,
            seasons=seasons,
            crops=crops,
            soil_type=soil_type,
            photo=photo,
            description=description,
        )
        item.save()

        
    return render(request, 'add.html')


from django.shortcuts import render 

def success(request):
    return render(request, 'add.html')

def index(request):
    return render(request, 'index.html')

def admin(request):
    return render(request, 'admin/base.html')

def admin_dashboard(request):
    from django.shortcuts import render
from .models import  Item

from django.shortcuts import render
from .models import Item

def admin_dashboard(request):
    from django.shortcuts import render
from .models import Item

def admin_dashboard(request):
  
    items = Item.objects.all()  # Fetch all items
    total_items = items.count()  # Count items
    print("Total Items:", total_items)  # Debugging output
    return render(request, 'admin/admin_dashboard.html', {'items': items, 'total_items': total_items})




    

def register(request):
    return render(request, 'admin/register.html')

def login(request):
    return render(request, 'admin/login.html')

def admin_settings(request):
    return render(request, 'admin/admin_settings.html')

def logout(request):
    return render(request, 'admin/logout.html')