from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    user = request.user
    # Retrieve any additional profile information here
    context = {
        'user': user,
        # Add additional context data as needed
    }
    return render(request, 'profile.html', context)


from django import forms
from .models import SellerProfile, Store


from django.shortcuts import render, redirect
from .forms import SellerProfileForm, StoreForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .forms import SellerProfileForm, StoreForm
from django.contrib.auth.decorators import login_required
from .models import SellerProfile

@login_required
def create_seller_and_store(request):
    try:
        seller_profile = request.user.sellerprofile
    except SellerProfile.DoesNotExist:
        # Create a new SellerProfile if not exists
        seller_profile = SellerProfile(user=request.user)
        seller_profile.save()

    if request.method == 'POST':
        seller_form = SellerProfileForm(request.POST, request.FILES, instance=seller_profile)
        store_form = StoreForm(request.POST, request.FILES)

        if seller_form.is_valid() and store_form.is_valid():
            seller_form.save()

            store = store_form.save(commit=False)
            store.owner = seller_profile
            store.save()

            return redirect('some-view')  # Replace with your desired redirect

    else:
        seller_form = SellerProfileForm(instance=seller_profile)
        store_form = StoreForm()

    return render(request, 'create_seller_and_store.html', {'seller_form': seller_form, 'store_form': store_form})



from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .forms import ProductForm, ProductImageForm
from .models import Product, ProductImage  # Import the ProductImage model here
from django.contrib.auth.decorators import login_required

# Your view function remains the same...


@login_required
def add_product(request):
    ImageFormSet = modelformset_factory(ProductImage, form=ProductImageForm, extra=3)
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=ProductImage.objects.none())

        if product_form.is_valid() and formset.is_valid():
            product = product_form.save(commit=False)
            product.seller = request.user.sellerprofile
            product.save()

            for form in formset.cleaned_data:
                if 'image' in form:
                    image = form['image']
                    photo = ProductImage(product=product, image=image)
                    photo.save()
            
            return redirect('some-view')  # Adjust the redirect as needed

    else:
        product_form = ProductForm()
        formset = ImageFormSet(queryset=ProductImage.objects.none())

    return render(request, 'add_product.html', {'product_form': product_form, 'formset': formset})


from django.shortcuts import render
from .models import Product

def homepage(request):
    products = Product.objects.filter(status='Available').order_by('-date_listed')
    return render(request, 'homepage.html', {'products': products})

from django.shortcuts import render

def accessibility_settings_view(request):
    return render(request, 'accessibility_settings.html')
