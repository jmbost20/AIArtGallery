from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.

from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items= Item.objects.filter(is_sold= False)[0:6]
    categories= Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

###Jonah Code
def logout_view(request):
    logout(request)
    return redirect('core:login')  # Replace 'core:login' with the appropriate URL pattern for your login page

###Jonah Code
def contact(request):
    return render(request, 'core/contact.html')

###Privacy
def privacy(request):
    return render(request, 'core/privacy.html')

###Privacy
def about(request):
    return render(request, 'core/about.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
 