from django.shortcuts import render,redirect
from item.models import Category, Item

from .forms import SignupForm

# This view renders the index page with items and categories
def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all() 

    return render(request, 'core/index.html', {'items': items, 'categories': categories})

def contact(request):
    return render(request, 'core/contact.html') 

def about(request):
    return render(request, 'core/about.html')

def terms(request):
    return render(request, 'core/t&c.html')

def privacy(request):
    return render(request, 'core/privacy_policy.html')

# This view handles user signup
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    form = SignupForm()
    return render (request,'core/signup.html',{'form':form})