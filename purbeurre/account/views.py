from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Merci {username}, votre compte a été créé avec succés, vous pouvez maintenant vous connecter')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


@login_required
def profile(request):
    user_id = request.user.pk
    user_profile = Profile.objects.get(pk=user_id)
    products = user_profile.favorite.all()
    context = {
        "products": products
    }
    return render(request, 'account/profile.html', context)
